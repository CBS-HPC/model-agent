# Provider workflow

Provider IDs distinguish `ucloud-vllm` (self-hosted) from `aitta` (managed LUMI).
`ucloud-ai` is a separate planned fixed platform; its catalog entry does not
authorize or implement requests. No command or fallback exists for it yet.

1. Gather requested model/task, context/concurrency and desired provider/control.
2. Inspect offline provider capabilities without allocating resources.
3. For AITTA, query the live catalog and model capability/worker status. For UCloud,
   delegate inspection/sizing/prepare to its explicit workspace and reviewed profile.
4. Explain the selected provider and constraints; candidates and plans are not launches.
5. Execute only the requested provider action. Keep existing authorization but never
   infer permission for GPU allocation from a sizing or documentation request.
6. Verify the actual task/endpoint and record provider-specific evidence and limits.

The CLI exposes explicit namespaces rather than pretending both providers share
job controls. UCloud owns lifecycle/journals and precise job identity. AITTA owns
workers and Slurm. No transparent fallback, duplicate allocation or model substitution.

UCloud Link/optional account-key setup delegates to the provider's separate
setup-plan/apply/status/reconcile/cleanup commands. Plan is read-only; apply/cleanup
preview until --yes, and resource writes need explicit target-specific intent.
These commands create no jobs and do not establish deployment readiness. Retain
provider-owned intent/receipts and created/reused ownership; unknown outcomes block
retries. No setup logic or second journal belongs in the wrapper. Both template
IDs remain required; application-spec bootstrap is not yet supported.

UCloud delegation requires a project workspace named ucloud-vllm-agent in its
pyproject.toml. Arguments retain their meaning; paths resolve there. No wrapper
credentials or settings are loaded first. Each invocation uses a child process
with that cwd; the wrapper's cwd/environment are not modified. Explicit inherited
environment remains higher precedence than the child's .env. Use the subprocess
CLI contract in docs/researcher-onboarding.md for harness integration.

AITTA uses its independent released client for control operations and the wrapper
for chat checks. Preload requested means loading accepted, not ready. Chat check
requires expected model, content, finish and completed SSE plus rejection of missing
and wrong credentials. Reports omit tokens and generated text. No automatic retries.

Failure in one provider never starts the other provider. Unknown UCloud submissions
must be reconciled using its provider journal. Release/stop applies only to an exact
operator-requested owned UCloud target; there is no AITTA worker shutdown command.
