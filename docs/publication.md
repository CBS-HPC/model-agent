# Publication checklist

The operator selected MIT for code and CC BY 4.0 for documentation, and chose to
sanitize historical operational details before public publication. This checklist
covers `model-agent`, `ucloud-vllm-agent` and `lumi-aitta-api`. The operator approved historical cleanup and public publication on 2026-10-20. The already public generic
`ucloud-api` project is separate; its release does not change provider pins here.

## Publication record — 2026-10-20

- The original provider and wrapper repositories are retained as private archives.
  Clean GitHub repositories reuse their public names, so cached pre-cleanup commits
  and earlier Actions logs remain in the private originals. Local backups also
  preserve the original refs and release files. No repository data was deleted.
- Provider and wrapper branch/tag histories were rewritten to replace operational
  identities with role labels and reserved example hostnames. Runtime files were
  checked against private backups. AITTA history needed no rewrite.
- Six attached source archives were sanitized: UCloud vLLM v0.1.2–v0.1.5 and
  CBS Model Agent v0.1.2–v0.1.3. The latter includes an additional archive whose
  documentation referenced rewritten commits. Their checksum files were updated;
  existing wheels were retained. Release notes identify the replacement date.
- The coordinated licensed public releases are wrapper v0.1.4, provider v0.1.6
  and AITTA API v0.1.1. The provider retains reviewed UCloud API v0.1.7; this
  publication change does not upgrade its runtime dependencies or host a model.
- License texts, build contents, retained refs/files, CI and a fresh installation
  are checked before public visibility. Project permissions and platform tokens
  are still required to operate UCloud or AITTA.

### Existing private checkouts

Commit identities and historical tag targets changed during the approved cleanup.
Create a fresh clone for future development; do not merge or force-push an old
checkout back into the cleaned repository. Preserve local .env files, SSH keys,
profiles and ignored ownership/deployment journals. Migrate your own local files
deliberately without uploading them or copying credentials between projects.
Existing runtime allocations and journals were not changed by publication.

## Tracked documentation

- Use descriptive role labels for historical jobs and Links, and reserved
  `example.org` hostnames for deployment URLs. These are documentation labels,
  not valid UCloud identifiers or usable endpoints.
- Use placeholders for drive IDs, deployment run IDs and compilation-cache
  identifiers. Keep exact operational identities in private, ignored journals.
- Omit the operator's project names and workstation paths. Never publish real
  environment files, credentials, private keys, notebook outputs or raw journals.
- Preserve validation dates, measured timings and counts, hardware/runtime
  settings, public model revisions and upstream source references. Removing an
  identifier must not change the reported test result or imply current uptime.
- Retain official service origins such as `aitta.csc.fi` and `cloud.sdu.dk`;
  these identify supported platforms rather than an operator's deployment.

The provider's validation guides and benchmark JSON use the same role labels
across repeated jobs and lifecycle transitions. They explain the sanitization
alongside the results. Runtime profiles, notebook code, credentials and local
deployment/ownership journals are not changed by this documentation cleanup.

## Historical copies and releases

A new documentation commit does not remove earlier content from Git history,
tags, GitHub source downloads or attached source archives. A new version alone
also leaves old release files accessible. The publication record above describes
the approved cleanup; apply the checklist below to future publication changes.

Before a visibility change:

1. Inventory every reachable branch/tag, attached release archive, release note
   and available Actions log for the removed operational details. Distinguish
   original source archives from wheels, which may contain fewer documents.
2. Preserve a private backup and prepare a reviewed history/release cleanup plan.
   Rewriting commits/tags changes commit IDs; removing or replacing release files
   changes availability or checksums. Neither follows implicitly from editing docs.
3. Resolve existing release pins before altering historical tags or files. Test a
   coordinated installation of the provider and wrapper after the chosen cleanup;
   preserve the separate AITTA client boundary and avoid dependency upgrades that
   are unrelated to publication.
4. Recheck the exact refs/files that will become public, including downloadable
   GitHub source archives and any retained logs. Confirm licenses and clean build
   contents. A prior secret scan does not establish this metadata-cleanup gate.
5. Change each required repository's visibility only on the operator's explicit
   publication instruction, then verify the documented installation path using
   access equivalent to a new researcher.

The cleanup inventory and original-to-role mapping are private audit artifacts;
do not commit them, copy them into release notes or attach them to public issues.

## Remaining acceptance

Publishing source does not complete colleague-led onboarding, authenticated AITTA
validation or additional model tests. Their existing workload/access gates remain
in force. See the [onboarding pilot plan](onboarding-plan.md) for those steps.
