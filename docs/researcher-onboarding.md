# Use CBS Model Agent in your own harness

For self-hosting, follow the provider's [researcher installation/setup guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/researcher-onboarding.md),
[CLI integration contract and copyable instructions](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/harness-integration.md)
and [operations guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/researcher-operations.md).
Install the ucloud-vllm extra only if you do not need AITTA. Keep the provider
checkout as your own project workspace; pip installation alone supplies neither
its profiles nor its local deployment records.

```sh
cbs-model providers
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent doctor
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent doctor --online --profile config/local.qwen.json
```

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
[Link/public-key setup guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/v0.1.5/docs/resource-setup.md)
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
[bootstrap guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/v0.1.5/docs/bootstrap.md)
when no prior jobs exist. `catalog --live` offers a read-only
queue snapshot, not a reservation or automatic model/machine selection.

Bootstrap commands are delegated unchanged:

```sh
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-plan --request config/local.bootstrap.json --output artifacts/bootstrap-plan.json
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent bootstrap-apply --plan artifacts/bootstrap-plan.json --state run/bootstrap/first
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent doctor --online --profile config/local.qwen.json --bootstrap run/bootstrap/first/bootstrap.json
cbs-model ucloud-vllm --workspace /absolute/path/ucloud-vllm-agent preview-profile --profile config/local.qwen.json --bootstrap run/bootstrap/first/bootstrap.json
```

Apply/credentials/finish/release preview until --yes. Bootstrap apply can allocate
one selected CPU job for up to an hour; actual deploy additionally prepares the
model on CPU and allocates the reviewed GPU duration. Credential provisioning is
a separate explicit selected-value SSH stdin operation with exclusive remote-file
creation. Finish verifies it and releases the bootstrap CPU, emitting the finalized
artifact used by the last two commands. Never create dummy GPU template jobs.
Unknown writes block retries; recovery/renewal/rollback preserve the recorded
bootstrap source. The wrapper owns no separate resource/deployment journal.

The [operator-led trial](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/v0.1.5/docs/bootstrap-live-validation.md)
passed actual-image nginx syntax and all seven checks per loopback/nginx/public
endpoint path. This is historical scoped evidence, not current uptime, new-project
PII validation or independent colleague acceptance.

UCloud AI is reserved as a future managed provider: it will have its own access,
credential, model catalog and verification requirements. Do not ask its eventual
users to provision nginx, SSH keys or GPU template jobs. AITTA is already a
separate managed provider; see lumi-aitta.md for its supported task/API boundary.
