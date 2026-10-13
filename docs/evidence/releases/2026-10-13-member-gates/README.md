# xr-dev 0.3.4: release packet

Objective: publish the already merged FW02 board and release-ancestry gates as
an exact patch version. The operator authorized this release wave on 2026-10-13.
Hub pins and global installation belong to the coordinating hub wave.

## Source and acceptance

- Source main: `3605d10998241235778262b34d5b59188bb29248`; [PR 5](https://github.com/ssheleg/xr-dev/pull/5).
- Eligible source check: [run 38336373890](https://github.com/ssheleg/xr-dev/actions/runs/38336373890), success.
- [Implementation packet](../../member-gates-20261013/README.md): 42 process controls,
  including 38 hostile plants and four valid shapes. The coordinator independently
  replayed the final Telegram controls and verified identical sibling helper/harness hashes.
- This release changes version metadata and evidence only; the source gate implementation
  and CI job bodies remain the merged, reviewed ones.

## Requirements and sequence

1. Synchronize package, marketplace, plugin, existing skill metadata and skill card
   to `0.3.4`; add the exact changelog section, preserving historical versions.
2. Run the owner's required local gate sequentially; strict manifest validation and
   payload dry-run supplement it. Record actual outcomes below.
3. Independently review the frozen diff, push a draft PR, then promote it once for
   eligible `ready_for_review` checks. Ordinary exact-head squash merge only.
4. Create a new annotated `v0.3.4` at merged canonical main, after confirming the
   tag and npm version are absent. Watch the existing release workflow, then verify
   the exact registry version and GitHub release. Never rewrite an old tag.
5. Hand source/tag/run receipts to the hub coordinator for pins and installation.

## Current state and next task

Plan committed before the metadata change. PR admission, tag creation, publication and installation remain pending.
Next: freeze this receipt, push, then promote the reviewed draft once. No model/provider/native-runtime acceptance is inferred.

Skills used: make-skill (release construction), task-pipeline (delivery),
agent-sync (local advisory ownership), evidence-docs (source and check receipts).

## Candidate review and payload

The coordinator independently reviewed `198ee49efaa53737e3872b160cc7adf2d18f58d9`: **PASS**. Version fields,
new changelog and existing skill metadata agree; there is no executable or workflow
diff. XR's card correction names the seven actual skill directories.

`npm pack --dry-run --json` exited 0: 39 files, 201455 unpacked bytes;
no `.env`, agent-sync state or Python cache residue. Both common gate files retain
the same SHA-256 digests as the independently reviewed FW02 source wave.

Draft [PR 6](https://github.com/ssheleg/xr-dev/pull/6) preserves the
no-per-push CI policy until local checks finish.

## Local candidate checks

`npm test`: 12 structural checks, seven skills and 25 references pass. `npm run test:negatives`: eight owner plants plus 42 member process controls pass. Installer: 11 cases pass. Both strict Claude manifests pass. `git diff --check` passes.
All test and strict-validation commands exited 0.
Local checks do not imply native/model or family-install acceptance.
