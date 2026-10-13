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

Published and byte-verified; see [the final receipt](#published-readback).
Next: coordinator reconciles family pins and global installation separately.
No model/provider/native-runtime acceptance is inferred.

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


## Published readback

The new annotated `v0.3.4` resolves to merged source
`4bd9e978ca6f73b73e91f26cd58b67323383c5f4`. [Release run 38340370423](https://github.com/ssheleg/xr-dev/actions/runs/38340370423)
completed successfully on that exact tag/source, and the [GitHub release](https://github.com/ssheleg/xr-dev/releases/tag/v0.3.4)
and exact npm package `@ssheleg/xr-dev@0.3.4` were observed.
No historical tag was changed.

The [owner machine receipt](published-readback.json) records registry integrity,
tarball SHA-256 and every packaged file's hash/size. All 39 files matched
tagged source byte-for-byte. Isolated `npm exec --yes --package=@ssheleg/xr-dev@0.3.4 -- xr-dev --help`
exited 0 without installing skills. The later repository-only header successor
`d36912f4a69be90b920ff7c15a890c805761b35c` also matched every published payload byte.

This follow-up closes GATE-01 and GATE-02's source/publication scope from observed
evidence. It changes documentation only, preserves package version and payload,
and does not claim installation, native agent use or older releases were tested.
Exact next task: coordinator consumes these final board states and publication
receipts in its family-pin/install wave.

Documentation reconciliation checks: `python3 test/validate.py` and
`git diff --check` exited 0. `npm pack --dry-run --json` exited 0; all
39 payload paths and SHA-256 hashes still matched the published receipt.
No implementation or test code changed, so the prior implementation gates remain
the source evidence; eligible PR validation will apply to this frozen successor.
