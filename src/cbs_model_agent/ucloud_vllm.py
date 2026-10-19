from __future__ import annotations

from importlib.util import find_spec
from pathlib import Path
import subprocess
import sys
import tomllib


def run(workspace: Path, arguments: list[str]) -> int:
    """Delegate in a child process; provider settings never enter this process."""
    workspace = workspace.resolve()
    manifest = workspace / "pyproject.toml"
    if not manifest.is_file() or tomllib.loads(manifest.read_text(encoding="utf-8-sig")).get(
            "project", {}).get("name") != "ucloud-vllm-agent":
        raise ValueError("--workspace must identify the UCloud vLLM agent project")
    if not arguments:
        raise ValueError("Supply a UCloud provider command, for example models or status")
    if find_spec("ucloud_vllm_agent") is None:
        raise ValueError("Install CBS Model Agent's [ucloud-vllm] extra before using this provider")
    # No shell, environment mutation or automatic retry. Inherit streams and
    # explicit caller environment; the child's .env supplies missing settings.
    return subprocess.run([sys.executable, "-m", "ucloud_vllm_agent", *arguments],
                          cwd=workspace, check=False).returncode
