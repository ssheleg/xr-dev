# Quest platform coverage handoff

Date: 2026-09-21. Branch `codex/xr-platform-coverage`, remote `git@github.com:ssheleg/xr-dev.git`; source base `7954ba2a884f5a71d7487981b4335c0ecdbc25d4`. [Specification and requirements](../../specs/2026-09-21-platform-coverage.md).

## Completed

Updated all six skill bodies and added seven task-triggered reference modules:

- [Project discovery/build/audit](../../../../plugins/xr-dev/skills/quest-native/references/project-playbook.md)
- [MR capabilities and lifecycle](../../../../plugins/xr-dev/skills/quest-native/references/mixed-reality.md)
- [Rendering experiments](../../../../plugins/xr-dev/skills/quest-perf/references/rendering-playbook.md)
- [Product and release readiness](../../../../plugins/xr-dev/skills/quest-store/references/production-readiness.md)
- [Spatial build/audit fallback](../../../../plugins/xr-dev/skills/quest-spatial/references/build-and-audit.md)
- [Research and tool navigation](../../../../plugins/xr-dev/skills/quest-tooling/references/research-navigation.md)
- [WebXR runtime/delivery](../../../../plugins/xr-dev/skills/quest-webxr/references/runtime-delivery.md)

Corrected the CPU/GPU sum, categorical stale-frame diagnosis, automatic thermal/rate claims, hard Spatial capacities, direct-MCP setup default and current Meta release launch category. Updated the native manifest reference and Spatial budget explanation. Added seven adverse scenarios and corrected existing expectations for gateway setup, measured panel estimates, missing companions and the merged APK as release evidence.

## Checks executed

| Check | Result |
|---|---|
| `npm test` | PASS: 11 checks, 6 skills, 17 references |
| `npm run test:negatives` | PASS: all 8 planted defects caught |
| `node test/installer_test.js` | PASS: 11 cases; all 11 temporary homes removed |
| `claude plugin validate . --strict` | PASS |
| `claude plugin validate plugins/xr-dev --strict` | PASS |
| `python3 test/evals_validate.py` | PASS: 18 trigger cases, 13 scenarios |
| `python3 test/evals_validate.py --self-test` | PASS: invalid trigger boolean detected |
| Bundled make-skill `audit_skill.py <skill-dir> --house`, each of six skills | PASS: zero gaps; [raw normalized outputs](house-audit.json) |
| External URLs in seven new references | 44/44 HTTP 200; [receipt](source-links.json) |
| `git diff --check` | PASS |

These results check packaging, structural contracts, installer behavior and source retrieval. [Model evaluation results](../../../../test/evals/RESULTS.md) remain explicitly unexecuted; authored scenarios are not passes. No engine/device/Store/GPU inference run occurred. Camera permission discrepancy is documented, not experimentally resolved here.

## Decisions, limits and next task

Retain six owners and use on-demand references. Ordinary engine implementation remains with existing Meta companions or the planned game-dev pack; vLLM-Omni is an optional off-device backend proposal in the family research, not a new xr-dev runtime dependency.

This branch intentionally keeps version 0.2.1 while under review. No release tag, installed skill, gateway config or parent submodule pin changed. Local-only: downloaded source documents, caches, credentials, model weights, private Foundry operations and device data must not enter this repository.

**Exact next task:** execute baseline-versus-candidate model cases s07–s13 in isolated sessions with the recorded neighboring skill set, then the affected existing cases. Record model/runtime/source versions and per-expectation results. Use a real target build/device for manifest, camera/account and performance claims; mark absent prerequisites NOT-RUN. Correct measured failures before performing the normal coordinated version bump/release and family pin update.

The central index is [the family XR/creative research](https://github.com/ssheleg/sshlg-skills/tree/codex/xr-creative-research/docs/evidence/research/2026-09-21-xr-creative). It links this member's exact pushed commit and the bounded implementation packets. A pushed branch is reviewable work, not a completed release.
