# Researcher onboarding pilot

Use this plan to onboard a colleague to **CBS Model Agent with UCloud vLLM**.
Technical installation/commands live in the provider's maintained
[onboarding guide](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/researcher-onboarding.md).
This plan defines the sequence, responsibilities and evidence needed to accept it.
Reviewed 2026-10-20 against wrapper v0.1.3, provider v0.1.5 and ucloud-api v0.1.7.

## Choose the user's route

| Need | Route |
| --- | --- |
| Call an existing UCloud endpoint | Receive its URL, served model name, serving credential and permitted use. No deployment setup. |
| Host a model in a new UCloud project/workspace | Follow phases 1–6 below with bootstrap. No prior job IDs needed. |
| Reuse compatible existing UCloud templates | Follow the same phases, substituting the two explicit template IDs for bootstrap. |
| Use an AITTA-managed model | Install the AITTA extra and follow [lumi-aitta.md](lumi-aitta.md). No self-hosted nginx, SSH or GPU selection. |
| Use UCloud AI | Separate future integration; no executable adapter yet. |

## Pilot phases

| Phase | Researcher and support actions | Completion evidence |
| --- | --- | --- |
| 1. Confirm access and workload | Project administrator confirms CPU/GPU allocation, permissions and a writable drive. Researcher obtains private Git read access, a UCloud token/its metadata ID and local SSH identity. Agree the small test model, context/concurrency, maximum duration and operator. | Exact project UUID, selected source mode, intended workload and allocation limits; credentials remain in local files. |
| 2. Install in isolation | Researcher creates a new parent directory, clones the paired release tags and creates an external venv. Install only the UCloud extra initially; leave other projects untouched. | Version commands report wrapper 0.1.3/provider 0.1.5; offline provider listing works. |
| 3. Configure and prepare resources | Fill the provider root .env locally. Select the drive, CPU product and own URL. If needed, review setup-plan and explicitly apply the Link/optional public-key changes. Record created/reused ownership. | Correct UUID/token ID/URL, local key selection and resource setup receipts. No job is required to reserve a Link. |
| 4. Bootstrap the workspace | Review bootstrap-plan for a fresh namespace. When that CPU allocation/folder work is requested, apply, explicitly provision credentials, then finish. Existing-template users verify both jobs and skip bootstrap. | Finalized bootstrap.json and released bootstrap CPU, or verified compatible template IDs. Preserve all journals. |
| 5. Deploy the first model | Copy the Qwen profile locally; review license/revision, machine, 4096 total context, concurrency 1 and one hour. Run size, prepare-profile, source-specific doctor/online preview. On the requested deployment, save the returned path and inspect verification. | Public expected-model/chat/SSE/auth checks pass; exact deployment/job IDs and expiry are recorded. Optional notebook uses the matching local profile/URL. |
| 6. Practise operation and handover | Invoke status through the researcher's own harness and locate recovery instructions. At the agreed end of the trial, explicitly release that owned deployment and confirm terminal job state. Decide separately whether to retain created Link/storage. | Researcher can locate the journal, distinguish stop/release and explain expiry/renewal. CPU/GPU trial allocations ended; retained resources are recorded. |

CPU/GPU allocation starts only at the relevant authorized apply/deploy stage.
Bootstrap permits a CPU job up to one hour; deployment can use another CPU job up
to one hour plus the requested GPU duration. Queue waits and first-time package/
model downloads vary. Do not promise a fixed session duration or monetary cost.

For the first pilot, use Qwen2.5-1.5B-Instruct on the supported B200 MIG baseline
if that product is available in the colleague's project. A different product or
workload requires review. PII, other architectures and additional live recovery
experiments are separate follow-ups, not hidden prerequisites for this chat pilot.

## Attach the researcher's harness

Give the harness the wrapper/provider AGENTS.md and WORKFLOW_CONTRACT.md and the
provider's [instruction snippet and subprocess contract](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/harness-integration.md).
Set an absolute provider workspace and use the intended venv executable. The
wrapper delegates; provider settings, profiles and journals stay in that workspace.
Do not assume pip installation automatically configures an AI harness or installs
an MCP server.

A suitable first request to the harness is:

> Read the CBS Model Agent and selected UCloud provider instructions. Help me set
> up a small Qwen chat model in my own UCloud project. Use a fresh namespace and
> the bootstrap path because I have no template IDs. Start by checking local
> installation and planning the exact resources. Show the CPU/GPU products,
> duration, storage path and URL before allocation. Keep credentials in the local
> provider .env and preserve every setup/deployment journal.

The request above starts planning. Execute the concrete allocation when the
researcher requests it; the instructions do not supply missing project/resources.
After a timeout, inspect status/journals instead of issuing a fresh deployment.

## Acceptance record

Record this in an ignored local artifact or approved support system, without
credentials, research data, raw service responses or notebook outputs:

- OS/Python, installed package versions and source tags.
- Selected project/source mode, drive/provider and CPU/GPU products.
- Guide steps completed and any undocumented prerequisites/interventions.
- Sanitized doctor/preview results, returned deployment path, task/auth results,
  allocation expiry and responsible operator.
- Trial release result, terminal CPU/GPU states and explicitly retained resources.
- Time spent on setup versus queue/install/download waits, and clarity problems.

Pilot acceptance requires the colleague to complete installation, deployment,
verification, harness status and exact-job release using the guide. Normal access
grants can come from an administrator; support must record every extra instruction
the guide failed to supply. Correct those gaps before onboarding a wider group.

## Current evidence and remaining limits

The operator-led 2026-10-20 trial already passed fresh-folder bootstrap, Link
setup, existing-key reuse, CPU preparation and Qwen checks through loopback,
nginx and public HTTPS. The actual released package chain also passed a fresh
non-editable installation. These are documented in the provider's
[trial record](https://github.com/CBS-HPC/ucloud-vllm-agent/blob/main/docs/bootstrap-live-validation.md),
and do not establish current uptime or independent colleague acceptance.

Still outside that evidence: new-drive creation (unsupported), a guided drive/CPU
picker, new-workspace PII, live key registration/removal, injected uncertain
folder/credential outcomes and bootstrap renewal/rollback. Existing automated
tests and older template-mode lifecycle validation cover parts of those paths.
AITTA authenticated live validation and UCloud AI integration remain separate.
