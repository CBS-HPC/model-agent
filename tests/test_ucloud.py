from pathlib import Path
import json
import os
import sys
from types import SimpleNamespace

import pytest

from cbs_model_agent.cli import main
from cbs_model_agent.ucloud_vllm import run


@pytest.fixture
def workspace(tmp_path):
    root = tmp_path / "provider"
    root.mkdir()
    (root / "pyproject.toml").write_text('[project]\nname = "ucloud-vllm-agent"\n')
    return root


def test_delegation_preserves_workspace_arguments_and_exit_code(workspace, monkeypatch):
    before = Path.cwd()
    calls = []
    def child(arguments, **options):
        calls.append((arguments, options))
        return SimpleNamespace(returncode=7)
    monkeypatch.setattr("cbs_model_agent.ucloud_vllm.find_spec", lambda _: object())
    monkeypatch.setattr("cbs_model_agent.ucloud_vllm.subprocess.run", child)
    assert main(["ucloud-vllm", "--workspace", str(workspace), "status", "--deployment", "deployments/exact/run"]) == 7
    assert calls == [([sys.executable, "-m", "ucloud_vllm_agent", "status", "--deployment", "deployments/exact/run"],
                      {"cwd": workspace, "check": False})]
    assert Path.cwd() == before


def test_failure_restores_cwd_and_never_falls_back(workspace, monkeypatch):
    before = Path.cwd()
    def child(*args, **kwargs):
        raise RuntimeError("synthetic failure")
    monkeypatch.setattr("cbs_model_agent.ucloud_vllm.find_spec", lambda _: object())
    monkeypatch.setattr("cbs_model_agent.ucloud_vllm.subprocess.run", child)
    assert main(["ucloud-vllm", "--workspace", str(workspace), "deploy"]) == 1
    assert Path.cwd() == before


def test_wrong_workspace_prevents_delegation(tmp_path):
    with pytest.raises(ValueError, match="workspace"):
        run(tmp_path, ["deploy"])


def test_argument_errors_have_schema_without_echoing_input(capsys):
    with pytest.raises(SystemExit) as caught:
        main(["--synthetic-private-argument"])
    assert caught.value.code == 2
    output = capsys.readouterr()
    assert not output.out and "synthetic-private-argument" not in output.err
    report = json.loads(output.err)
    assert report["schema"] == "cbs.model.error.v1"
    assert report["error"]["code"] == "invalid_arguments"


def test_two_workspaces_keep_settings_in_separate_real_children(tmp_path, monkeypatch, capfd):
    # A fake provider uses the same setdefault pattern as the real environment
    # loader. Real child processes prove the boundary, without UCloud credentials.
    package = tmp_path / "packages" / "ucloud_vllm_agent"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("")
    (package / "__main__.py").write_text(
        "import os,json\nfrom pathlib import Path\n"
        "key,value=Path('.env').read_text().strip().split('=',1)\n"
        "os.environ.setdefault(key,value)\nprint(json.dumps({'project':os.environ[key]}))\n")
    monkeypatch.syspath_prepend(str(package.parent))
    monkeypatch.setenv("PYTHONPATH", str(package.parent))
    monkeypatch.delenv("UCLOUD_PROJECT", raising=False)
    for name in ("researcher-A", "researcher-B"):
        workspace = tmp_path / name
        workspace.mkdir()
        (workspace / "pyproject.toml").write_text('[project]\nname="ucloud-vllm-agent"\n')
        (workspace / ".env").write_text("UCLOUD_PROJECT=" + name)
        assert run(workspace, ["doctor"]) == 0
        assert json.loads(capfd.readouterr().out)["project"] == name
        assert "UCLOUD_PROJECT" not in os.environ


def test_offline_providers_need_no_credentials(capsys):
    assert main(["providers"]) == 0
    output = capsys.readouterr().out
    assert "ucloud-vllm-agent@v0.1.6" in output
    assert "lumi-aitta-api@v0.1.1" in output
    import json
    providers = json.loads(output)
    assert providers["ucloud-vllm"]["mode"] == "self-hosted"
    assert "application bootstrap" in providers["ucloud-vllm"]["capabilities"]
    assert providers["ucloud-ai"]["status"] == "planned"
    assert providers["ucloud-ai"]["capabilities"] == []
