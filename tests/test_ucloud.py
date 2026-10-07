from pathlib import Path
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
    def provider_main(arguments):
        calls.append((Path.cwd(), arguments))
        return 7
    monkeypatch.setitem(sys.modules, "ucloud_vllm_agent.cli", SimpleNamespace(main=provider_main))
    assert main(["ucloud-vllm", "--workspace", str(workspace), "status", "--deployment", "deployments/exact/run"]) == 7
    assert calls == [(workspace, ["status", "--deployment", "deployments/exact/run"])]
    assert Path.cwd() == before


def test_failure_restores_cwd_and_never_falls_back(workspace, monkeypatch):
    before = Path.cwd()
    def provider_main(arguments):
        raise RuntimeError("synthetic failure")
    monkeypatch.setitem(sys.modules, "ucloud_vllm_agent.cli", SimpleNamespace(main=provider_main))
    assert main(["ucloud-vllm", "--workspace", str(workspace), "deploy"]) == 1
    assert Path.cwd() == before


def test_wrong_workspace_prevents_delegation(tmp_path):
    with pytest.raises(ValueError, match="workspace"):
        run(tmp_path, ["deploy"])


def test_offline_providers_need_no_credentials(capsys):
    assert main(["providers"]) == 0
    output = capsys.readouterr().out
    assert "ucloud-vllm-agent@v0.1.2" in output
    assert "lumi-aitta-api@v0.1.0" in output
    import json
    providers = json.loads(output)
    assert providers["ucloud-vllm"]["mode"] == "self-hosted"
    assert providers["ucloud-ai"]["status"] == "planned"
    assert providers["ucloud-ai"]["capabilities"] == []
