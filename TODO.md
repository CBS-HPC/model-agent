# Remaining work

Publication note: historical operational identifiers use role labels and example URLs; measurements and runtime behavior are retained. Exact identities belong in private journals.

## Isolated bootstrap follow-up (2026-10-20)

Provider v0.1.5 is published at v0.1.5 after Windows/Linux CI, source/wheel asset
checks and an isolated live Qwen bootstrap trial without prior job IDs. This
wrapper change pins that published release, adds bootstrap metadata/docs and keeps
generic control/journals in the provider. Remaining: wrapper v0.1.3 CI/publication
and fresh installation of the actual released chain. Do not republish the provider.

The trial used operator-selected "isolated validation project", fresh namespaced storage
and Link, and new local sandbox credentials. Both CPU jobs were released. Serving
job bootstrap-qwen-gpu has recorded expiry 2026-10-20 14:04:09 Copenhagen; query status before
claiming uptime. Never renew/replace/release implicitly. Original checkouts and
deployed folder remain untouched. See sibling docs/bootstrap-live-validation.md
for exact scope, recovery and limits. Colleague-led acceptance and new-workspace
PII remain distinct from this operator-led trial.

## Researcher onboarding priority

- [x] Follow the local/harness stage of the [UCloud vLLM onboarding roadmap](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/TODO.md#researcher-onboarding-roadmap):
  clear installation/access/workspace requirements, readiness checks and a
  subprocess CLI integration contract for researchers' own AI harnesses.
- [x] Add a wrapper onboarding guide and copyable harness instructions explaining
  provider selection, cwd/settings, JSON/exit codes and resource-allocation intent.
- [x] Isolate UCloud delegation in a child process per invocation and regression
  test two workspaces. Repeated direct provider-main embedding remains unsupported.
- [x] Pin the released UCloud vLLM provider v0.1.3 for the onboarding changes.
- [x] Document optional Link/account-public-key setup through released ucloud-api
  v0.1.7 and published provider v0.1.4. Keep resource control and ownership/recovery
  journals in the provider/API; the wrapper delegates without duplicating them.
- [x] Update optional dependencies and offline capabilities to published provider
  v0.1.4, including separate setup and opt-in live availability snapshots.
- [ ] Validate clean installation and a first deployment using another
  researcher's project. Local/mock validation and release publication are separate
  from this outstanding live acceptance test.
- [x] Publish wrapper v0.1.1 with wheel/source/checksums and passing Windows/Linux
  CI on Python 3.11/3.13. Fresh local installation of actual released dependencies
  passed offline discovery, doctor, template export and synthetic preparation.
- [ ] Keep the future UCloud AI onboarding separate: review its own access,
  authentication and model/task contract rather than requiring self-hosting setup.

Continuation checkpoint 2026-10-20: provider v0.1.4 is published at v0.1.4 with
128 passing local tests (one platform skip), passing Windows/Linux CI and reviewed
ucloud-api v0.1.7. Wrapper v0.1.2 consumes that published provider and documents
separate Link/key setup. Wrapper v0.1.2 (v0.1.2) is published with wheel/source/
checksums, 17 passing local tests and passing Windows/Linux CI on Python 3.11/3.13.
Fresh installed release-chain checks passed delegation, doctor, assets and mocked
read-only setup. Do not repeat completed checks/publication; inspect GitHub first.
No cloud jobs/resources were created. Shared storage/bootstrap,
new setup-adapter live validation and colleague-led onboarding remain pending.

Previous checkpoint 2026-10-19: local harness changes and provider pin are
published in wrapper v0.1.1 (v0.1.1), consuming provider v0.1.3 (v0.1.3).
Both CI matrices passed; 17 wrapper tests pass locally. No cloud jobs/resources were created. Link/key
provisioning, no-prior-job bootstrap and colleague-led live onboarding remain
pending; consult the provider's roadmap and latest released API before proceeding.

## Provider development

- [ ] Add the distinct UCloud AI fixed inference platform (`ucloud-ai`) later;
  review its access/API/catalog and task contracts before implementing an adapter.

- [x] Independent UCloud and LUMI providers behind CBS Model Agent.
- [x] Explicit UCloud workspace delegation without duplicated settings/journals.
- [x] Migrate AITTA discovery/preload/chat verification out of the UCloud agent.
- [x] Independent optional provider dependencies and offline capability listing.
- [ ] Authenticated AITTA live validation with an operator-selected model/token.
- [ ] Embedding/classification task verification when required by a workload.
- [ ] Unified request planning and provider comparison backed by actual evidence.
- [ ] Cross-provider benchmarks using comparable workloads and documented limits.
