# CBS Model Agent

A conversational workspace and deterministic Python entry point for choosing and
using open-weight inference providers. Codex/Claude handles the conversation;
provider packages perform the requested operations.

| Provider | Ownership | Use when |
| --- | --- | --- |
| [UCloud vLLM agent](https://github.com/CBS-HPC/ucloud-vllm-agent) | Model inspection, sizing, pinned profiles, jobs, nginx, chat/PII verification and lifecycle | You need a custom HF model/revision, task adapter or control over machine/configuration |
| [LUMI AITTA API](https://github.com/CBS-HPC/lumi-aitta-api) | Token authentication, service/model/worker discovery and explicit preload | Your desired model is offered by the managed AITTA service |
| [UCloud AI](https://ai.escience.sdu.dk/) — planned | Fixed managed inference platform; future adapter | Future option for its platform-provided models |

`ucloud-vllm` means self-hosting with vLLM on a machine you select. `ucloud-ai`
is reserved for the separate UCloud AI platform and is listed as planned only;
it has no executable commands, credentials or assumed API compatibility yet.

CBS Model Agent owns provider selection, the combined request workflow and AITTA
chat/SSE/auth verification. UCloud remains a self-contained inference provider;
it does not import LUMI. The LUMI client does not import UCloud. No cross-provider
fallback, bulk loading, job allocation or renewal runs automatically.

## Install

Start with [researcher onboarding and harness integration](docs/researcher-onboarding.md)
for installation, provider workspace requirements and the command/result contract.

```powershell
python -m pip install -e ".[providers]"
cbs-model providers
```

Private Git dependencies require GitHub access. Install `.[ucloud-vllm]` or `.[aitta]`
instead if you only use one provider. The pins are UCloud agent v0.1.4 and LUMI
API v0.1.0. `providers` is offline and works without optional dependencies.

## UCloud vLLM

From the `model-agent` folder, use the sibling provider workspace so its `.env`, profiles, notebooks, deployment
journals and cache settings remain in their established locations:

```powershell
cbs-model ucloud-vllm --workspace "..\ucloud-vllm-agent" models
cbs-model ucloud-vllm --workspace "..\ucloud-vllm-agent" size --profile config/hosting.qwen-small.json
cbs-model ucloud-vllm --workspace "..\ucloud-vllm-agent" status --deployment deployments/name/run-id
```

Arguments are delegated directly to the provider CLI in that workspace. Deployment
and destructive commands keep the provider's review/ownership requirements. The
wrapper never creates a second journal or translates templates/jobs itself.
Read the UCloud repository's AGENTS.md and WORKFLOW_CONTRACT.md before operations.

Delegation uses a separate child process per invocation. Provider-loaded settings
cannot leak into subsequent workspace calls; explicit inherited environment
variables still override that workspace's .env. Success output is JSON, deployment
progress is on stderr, and errors include a structured JSON record.

Provider v0.1.4 consumes released ucloud-api v0.1.7. Optional first-time
[Link/public-key setup](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/v0.1.4/docs/resource-setup.md)
has separate preview/apply/reconcile/cleanup commands and creates no jobs. It
preserves created/reused ownership and blocks uncertain outcomes. `catalog --live`
adds queue evidence without changing model sizing or automatically selecting a
machine. Shared-folder/template setup and bootstrap without prior job IDs remain
separate; deployment still requires both explicit template IDs.

## LUMI AITTA

Use a local `AITTA_API_KEY`, or reference an existing local environment file with
`aitta --env-file`. No credentials are copied, moved or uploaded.

```powershell
cbs-model aitta models
cbs-model aitta status
cbs-model aitta workers --model "vendor/model-from-the-live-list"
cbs-model aitta preload --model "vendor/model-from-the-live-list"
cbs-model aitta check --model "vendor/model-from-the-live-list"
```

Preload and inference can start an offline model on shared LUMI resources; both
require an explicit request to use that model. AITTA selects hardware and owns
workers. Its live model catalog is distinct from UCloud's validated model history.
Read [AITTA setup and limits](docs/lumi-aitta.md).

## Evidence and development

UCloud's dated validation stays with its provider; it is not a current uptime
claim. AITTA has local contract tests; authenticated live validation is pending.
There is no uniform claim of production availability across providers.

```powershell
python -m pip install -e ".[dev]"
python -m pytest
python -m build
```

See [architecture](docs/architecture.md), [execution contract](WORKFLOW_CONTRACT.md)
and [remaining work](TODO.md). No live jobs are started by the test suite.
