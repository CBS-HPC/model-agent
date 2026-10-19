# Remaining work

## Researcher onboarding priority

- [ ] Follow the [UCloud vLLM onboarding roadmap](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/TODO.md#researcher-onboarding-roadmap):
  clear installation/access/workspace requirements, readiness checks and a
  subprocess CLI integration contract for researchers' own AI harnesses.
- [ ] Add a wrapper onboarding guide and copyable harness instructions explaining
  provider selection, cwd/settings, JSON/exit codes and resource-allocation intent.
- [ ] Fix/test settings isolation before advertising repeated in-process Python
  embedding across provider workspaces; use a subprocess per invocation initially.
- [ ] After a provider release, update its dependency pin and document optional
  resource setup through released ucloud-api Link management. SSH public-key
  management is conditional on upstream delivery. Keep implementation in the
  provider/API; the wrapper must not duplicate resource control or journals.
- [ ] Validate clean installation and a first deployment using another
  researcher's project, then publish the updated wrapper release.
- [ ] Keep the future UCloud AI onboarding separate: review its own access,
  authentication and model/task contract rather than requiring self-hosting setup.

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
