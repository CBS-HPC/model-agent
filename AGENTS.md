# CBS Model Agent

This is the cross-provider conversational workspace for open-weight inference.
Respond in the operator's language; repository text is English. Read README.md,
WORKFLOW_CONTRACT.md and docs/architecture.md before changing the workflow.

Choose UCloud for custom HF revisions/adapters and explicit machine/configuration
control; choose AITTA for models currently offered by its managed service. Explain
capability/availability limits. Do not silently choose a fallback or assume task
equivalence because both expose OpenAI-compatible chat. Ask only for missing
provider/workload decisions. Keep existing deployment authorization in scope.

Consume pinned released provider packages. Generic LUMI API transport/preload
belongs to lumi-aitta-api; UCloud sizing/jobs/lifecycle belongs to ucloud-vllm-agent.
Do not edit provider repositories as part of routine requests or reimplement job
submission. Read the selected UCloud workspace's AGENTS.md and workflow contract
before remote actions. Delegate with its explicit --workspace; preserve relative
profiles, journals and secrets there. Never load the wrapper .env before delegation.

Read-only discovery is ordinary setup. Preload/inference can consume LUMI capacity;
UCloud deploy/replace/rollback/renew can allocate GPU time. Require explicit user
intent for those operations. Never bulk preload, automatically switch providers,
retry unknown submissions, stop shared workers or renew after an operator stops.
Preload accepted is not readiness. Never stop a successfully hosted job on exit.

Never print secrets or raw authenticated responses. Do not read .env into model
context, copy it between workspaces, rewrite it, upload tokens or put keys in CLI
arguments. Code may load an existing environment file. AITTA_API_KEY and
VLLM_API_KEY are different credentials; no fallback between them.

AITTA verification is chat/SSE/auth only. PII remains a UCloud-specific task;
classification/embedding require their own tested paths. Preserve source/revision,
hardware and settings with evidence. Historical validation is not current uptime.
No authenticated live AITTA validation exists yet. Contract tests use local/mock
transport. No jobs should start for docs, tests or architecture changes.

Keep provider metadata and documentation synchronized. Do not commit detailed
runtime journals, environment files, generated notebook outputs or credentials.
