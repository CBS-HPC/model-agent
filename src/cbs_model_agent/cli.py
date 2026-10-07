from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from . import __version__


PROVIDERS = {
    "ucloud-vllm": {"name": "UCloud vLLM", "status": "implemented", "mode": "self-hosted", "machine_selection": "provider agent",
               "capabilities": ["HF inspection", "sizing", "deployment", "chat", "PII", "lifecycle"],
               "dependency": "ucloud-vllm-agent@v0.1.2", "workspace_required": True},
    "aitta": {"name": "LUMI AITTA", "status": "implemented", "mode": "managed LUMI inference", "machine_selection": "AITTA service",
              "capabilities": ["model discovery", "worker status", "preload", "chat verification"],
              "dependency": "lumi-aitta-api@v0.1.0", "live_validation": "pending"},
    "ucloud-ai": {"name": "UCloud AI", "status": "planned", "mode": "fixed managed inference platform",
                  "homepage": "https://ai.escience.sdu.dk/", "capabilities": [],
                  "note": "Future integration; API, access and task contracts have not been reviewed."},
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CBS Model Agent: UCloud vLLM and LUMI AITTA inference")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="provider", required=True)
    commands.add_parser("providers", help="Offline provider capabilities; no network requests")
    command = commands.add_parser("ucloud-vllm", help="Delegate to the UCloud agent in its workspace")
    command.add_argument("--workspace", type=Path, required=True)
    command.add_argument("arguments", nargs=argparse.REMAINDER)
    command = commands.add_parser("aitta", help="LUMI managed inference")
    command.add_argument("--env-file", type=Path, default=Path(".env"), help="Existing local settings; never copied")
    actions = command.add_subparsers(dest="action", required=True)
    actions.add_parser("models")
    actions.add_parser("status")
    for action in ("workers", "preload"):
        item = actions.add_parser(action)
        item.add_argument("--model", required=True)
    item = actions.add_parser("check", help="Synthetic chat/SSE/auth requests; may load a model")
    item.add_argument("--model", required=True)
    item.add_argument("--timeout", type=int, default=300)
    item.add_argument("--output", type=Path, default=Path("artifacts/aitta-checks.json"))
    args = parser.parse_args(argv)
    try:
        if args.provider == "providers":
            print(json.dumps(PROVIDERS, indent=2))
            return 0
        if args.provider == "ucloud-vllm":
            from .ucloud_vllm import run
            arguments = args.arguments[1:] if args.arguments[:1] == ["--"] else args.arguments
            # Load no wrapper environment before delegating. Provider owns .env/state.
            return run(args.workspace, arguments)
        try:
            from lumi_aitta_api.settings import load_env
        except ImportError:
            raise ValueError("Install CBS Model Agent's [aitta] extra before using this provider") from None
        load_env(args.env_file)
        from . import aitta
        if args.action == "models":
            result = aitta.list_models()
        elif args.action == "status":
            result = aitta.service_status()
        elif args.action in ("workers", "preload"):
            result = getattr(aitta, args.action)(args.model)
        else:
            result = aitta.check_model(args.model, timeout=args.timeout)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2))
        return 0 if result.get("passed", True) else 1
    except (ValueError, OSError, RuntimeError, ImportError) as exc:
        # Only the independently maintained API client defines sanitized errors.
        safe_api_error = type(exc).__module__ == "lumi_aitta_api.client" and type(exc).__name__ == "AittaError"
        reason = str(exc) if isinstance(exc, ValueError) or safe_api_error else type(exc).__name__
        print("Operation failed: " + reason, file=sys.stderr)
        return 1
