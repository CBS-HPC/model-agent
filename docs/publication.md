# Publication checklist

The operator selected MIT for code and CC BY 4.0 for documentation, and chose to
sanitize historical operational details before public publication. This checklist
covers `model-agent`, `ucloud-vllm-agent` and `lumi-aitta-api`. They remain private
while the history and release cleanup is resolved. The already public generic
`ucloud-api` project is separate; its release does not change provider pins here.

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
also leaves old release files accessible. Keep visibility private until the
operator has approved how those historical copies should be handled.

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
