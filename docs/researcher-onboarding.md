# Use CBS Model Agent in your own harness

Start with the [onboarding pilot plan](onboarding-plan.md) for the phase sequence,
operator responsibilities and acceptance checklist. For a new UCloud installation,
clone wrapper v0.1.3 and provider v0.1.5 and follow the provider guide's Windows/Linux
venv/install instructions. The wrapper's UCloud extra installs released provider
code; pip installation does not automatically configure a coding harness.

For self-hosting, follow the provider's [researcher installation/setup guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/researcher-onboarding.md),
[CLI integration contract and copyable instructions](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/harness-integration.md)
and [operations guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/researcher-operations.md).
These maintained guides include clarifications after the tags; the command
examples target the released pair above. Install the ucloud-vllm extra only if
you do not need AITTA. Keep the provider
checkout as your own project workspace; pip installation alone supplies neither
its profiles nor its local deployment records.

```sh
cbs-model providers
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent doctor
```

The plain doctor command selects existing-template mode. If you have no job IDs,
complete bootstrap first, then use the explicit artifact in the commands below;
missing IDs at this stage are not a reason to allocate a dummy GPU.

Use an absolute path and the intended venv executable. Each UCloud invocation
runs in a separate child process with cwd set to that workspace. The wrapper
does not read its own .env first, change its own cwd or retain settings loaded
by the child. Explicit inherited environment still overrides the provider's .env.
Use subprocess CLI invocation as your harness interface, not repeated main()
calls in a shared application process. AITTA's direct Python CLI entry point is
also not a settings-isolated embedding API.

UCloud success stdout contains one provider-specific JSON value. Errors carry
a schema and error code on stderr; progress may precede the final JSON error
line. Help/version remain text. Exit 0 means that command succeeded, 1 is an
operation/requirements/check failure, and 2 is an argument/review/dependency gate
or uncertain resource outcome requiring reconciliation.
The wrapper propagates the provider's exit code unchanged. A timeout is not
cancellation or proof that a job was not created; use the provider journal.

Planning does not authorize allocation. Read the selected provider's contract
before calling a mutating action. Keep one authoritative set of provider journals,
and do not silently switch providers or substitute a model. API credentials and
task/data-use approval are separate decisions.

## Optional first-time UCloud resources

The pinned provider v0.1.5 uses released ucloud-api v0.1.7. Follow its
[Link/public-key setup guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/resource-setup.md)
to prepare a researcher-owned request, then delegate its preview commands:

```sh
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent setup-plan --request config/local.setup.json --output artifacts/setup-plan.json
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent setup-apply --plan artifacts/setup-plan.json --state run/setup/first
```

Only add `--yes` after the operator requests those exact resource changes. Setup
starts no CPU/GPU jobs, creates no secrets and writes no .env. SSH registration is
optional and account-scoped. Preserve the provider's receipt/ownership directory;
reconcile uncertain results instead of retrying. Cleanup protects reused resources
and is independent of job release. Shared storage/uploads use the separate
[bootstrap guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/bootstrap.md)
when no prior jobs exist. `catalog --live` offers a read-only
queue snapshot, not a reservation or automatic model/machine selection.

Bootstrap commands are delegated unchanged:

```sh
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-plan --request config/local.bootstrap.json --output artifacts/bootstrap-plan.json
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-apply --plan artifacts/bootstrap-plan.json --state run/bootstrap/first
```

The preceding apply is a preview. After the operator requests that planned CPU/
folder work, apply and explicitly provision/finish (remote key creation is its
own selected-value action):

```sh
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-apply --plan artifacts/bootstrap-plan.json --state run/bootstrap/first --yes
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-credentials --state run/bootstrap/first
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-credentials --state run/bootstrap/first --yes
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-finish --state run/bootstrap/first
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-finish --state run/bootstrap/first --yes
```

Only after finish emits the finalized source, prepare your local model profile
and run read-only checks:

```sh
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent doctor --bootstrap run/bootstrap/first/bootstrap.json
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent doctor --online --profile config/local.qwen.json --bootstrap run/bootstrap/first/bootstrap.json
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent preview-profile --profile config/local.qwen.json --bootstrap run/bootstrap/first/bootstrap.json
```

Apply/credentials/finish/release preview until --yes. Bootstrap apply can allocate
one selected CPU job for up to an hour; actual deploy additionally prepares the
model on CPU and allocates the reviewed GPU duration. Credential provisioning is
a separate explicit selected-value SSH stdin operation with exclusive remote-file
creation. Finish verifies it and releases the bootstrap CPU, emitting the finalized
artifact used by doctor/preview/deploy. Never create dummy GPU template jobs.
Unknown writes block retries; recovery/renewal/rollback preserve the recorded
bootstrap source. The wrapper owns no separate resource/deployment journal.

On the separately requested, reviewed model deployment:

```sh
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent deploy --profile config/local.qwen.json --bootstrap run/bootstrap/first/bootstrap.json --reviewed
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent status --deployment deployments/NAME/RUN
```

Use the returned deployment path. Release it explicitly at the agreed trial end;
stop retains the allocation. Template users omit --bootstrap FILE and supply both
job IDs. Recovery/replacement/renewal/rollback use the stored source, not a new
source argument. Do not mix either mode's resources or bypass uncertain journals.

The [operator-led trial](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/bootstrap-live-validation.md)
passed actual-image nginx syntax and all seven checks per loopback/nginx/public
endpoint path. This is historical scoped evidence, not current uptime, new-project
PII validation or independent colleague acceptance.

UCloud AI is reserved as a future managed provider: it will have its own access,
credential, model catalog and verification requirements. Do not ask its eventual
users to provision nginx, SSH keys or GPU template jobs. AITTA is already a
separate managed provider; see lumi-aitta.md for its supported task/API boundary.
