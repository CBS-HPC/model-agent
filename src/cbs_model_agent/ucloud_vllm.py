from __future__ import annotations

import os
from pathlib import Path
import tomllib


def run(workspace: Path, arguments: list[str]) -> int:
    """Delegate unchanged arguments in the explicit provider workspace."""
    workspace = workspace.resolve()
    manifest = workspace / "pyproject.toml"
    if not manifest.is_file() or tomllib.loads(manifest.read_text(encoding="utf-8-sig")).get(
            "project", {}).get("name") != "ucloud-vllm-agent":
        raise ValueError("--workspace must identify the UCloud vLLM agent project")
    if not arguments:
        raise ValueError("Supply a UCloud provider command, for example models or status")
    try:
        from ucloud_vllm_agent.cli import main
    except ImportError:
        raise ValueError("Install CBS Model Agent's [ucloud-vllm] extra before using this provider") from None
    previous = Path.cwd()
    try:
        os.chdir(workspace)
        return main(arguments)
    finally:
        os.chdir(previous)
