# Remaining work

## Public publication (2026-10-20)

The operator approved historical cleanup and public publication. All reachable
provider/wrapper branches and tags were sanitized with private backups retained;
six source archives and their checksum files were updated for operational details
or references to rewritten commits. Existing wheel runtime code was preserved.
New licensed releases are UCloud vLLM v0.1.6, AITTA API v0.1.1 and CBS Model Agent
v0.1.4. The UCloud API runtime pin remains v0.1.7. See the wrapper's
docs/publication.md for the scope and migration instructions. Older publication
checkpoints below are historical. Live colleague/AITTA acceptance remains pending.

Publication note: historical operational identifiers use role labels and example URLs; measurements and runtime behavior are retained. Exact identities belong in private journals.

## Publication cleanup (2026-10-20)

The operator chose sanitization. Tracked documentation now uses role labels and
example deployment URLs; historical project/job/resource/drive/run/cache
identifiers are omitted. Measurements, model revisions and hardware settings are
retained. Follow docs/publication.md before changing repository visibility.
Earlier commits/tags and attached source archives still require a separate,
reviewed cleanup decision; new documentation commits do not erase those copies.
This gate was subsequently resolved in the public publication record above.

## Licensing (2026-10-20)

The operator selected MIT for code and CC BY 4.0 for documentation. LICENSE.md
defines the split, including configuration/code examples and notebook cells;
LICENSES/ carries the full texts. Package metadata declares the combined SPDX
expression and includes both texts in new builds. Existing tags/release assets
and provider dependency pins are unchanged. Repository visibility and historical
copy cleanup are tracked above. Isolated wheel and
source builds were verified to include the scope notice, both full license texts
and the SPDX metadata.

## Documentation review (2026-10-20)

Reviewed wrapper/provider documentation against the published wrapper v0.1.3,
provider v0.1.5 and ucloud-api v0.1.7 pair/chain. Added docs/onboarding-plan.md for
the colleague-led pilot, linked the canonical provider install guide and fixed
bootstrap examples to include explicit apply/credentials/finish before doctor.
Clarified optional dependencies, AITTA working directory and future provider limits.
Documentation changes do not establish new live validation or colleague acceptance.
Cross-repository offline QA passed all 102 relative links and 108 CLI examples;
notebook code/output checks and the bundled hosting-skill validator also passed.
The changes clarify the published pair; they do not change its release tags/pins.

## Isolated bootstrap follow-up (2026-10-20)

Provider v0.1.5 is published at v0.1.5 after Windows/Linux CI, source/wheel asset
checks and an isolated live Qwen bootstrap trial without prior job IDs. This
wrapper pins that published release, adds bootstrap metadata/docs and keeps
generic control/journals in the provider. Wrapper v0.1.3 is published at v0.1.3
with wheel/source/checksums, 17 passing local tests and passing Windows/Linux
Python 3.11/3.13 CI. A fresh non-editable install of the actual 0.1.3/0.1.5/0.1.7
releases passed version/origin checks, wrapper delegation, local bootstrap doctor,
read-only preview, existing live-job/process status and pip check. It allocated
no jobs. Do not repeat publication or completed checks; inspect release state.

The trial used an operator-selected isolated validation project, fresh namespaced storage
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
- [x] Pin the released UCloud vLLM provider v0.1.5 for bootstrap onboarding.
- [x] Document optional Link/account-public-key setup through released ucloud-api
  v0.1.7 and published provider v0.1.4. Keep resource control and ownership/recovery
  journals in the provider/API; the wrapper delegates without duplicating them.
- [x] Update optional dependencies and offline capabilities to published provider
  v0.1.5, including separate setup, bootstrap and opt-in live availability snapshots.
- [ ] Validate clean installation and a first deployment using another
  researcher's project. Local/mock validation and release publication are separate
  from this outstanding live acceptance test.
- [x] Publish wrapper v0.1.3 with wheel/source/checksums and passing Windows/Linux
  CI on Python 3.11/3.13. Fresh local installation of actual released dependencies
  passed offline discovery, doctor, template export and synthetic preparation.
- [ ] Keep the future UCloud AI onboarding separate: review its own access,
  authentication and model/task contract rather than requiring self-hosting setup.

Historical checkpoint before v0.1.3 (superseded above): provider v0.1.4 is published at v0.1.4 with
128 passing local tests (one platform skip), passing Windows/Linux CI and reviewed
ucloud-api v0.1.7. Wrapper v0.1.2 consumes that published provider and documents
separate Link/key setup. Wrapper v0.1.2 (v0.1.2) is published with wheel/source/
checksums, 17 passing local tests and passing Windows/Linux CI on Python 3.11/3.13.
Fresh installed release-chain checks passed delegation, doctor, assets and mocked
read-only setup. Do not repeat completed checks/publication; inspect GitHub first.
No cloud jobs/resources were created. Shared storage/bootstrap,
new setup-adapter live validation and colleague-led onboarding remain pending.

Historical checkpoint 2026-10-19 (superseded above): local harness changes and provider pin are
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
