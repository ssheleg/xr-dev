# xr-dev: handoff

## 2026-10-20: v0.4.0, short router descriptions

Objective: free Claude Code's shared skill-listing budget (about 30,000 chars; 81 of
134 skills showed no description on 2026-10-20). The seven descriptions are now
415-456 chars (5,887 to 3,076 in total); removed trigger phrases moved verbatim into
each body's `## Triggers`. `test/validate.py` caps a description at 500 chars. Checks:
`npm test`, `npm run test:negatives`, `node test/installer_test.js` and both
`claude plugin validate --strict` runs exit 0. Open: the umbrella's advertised-trigger
check still reads descriptions only and reports 18 body-only triggers until its
context-diet change lands; the umbrella re-pin is the umbrella's task, not this
release's. Exact next task: none in this repository for this change.

## Earlier: evidence navigation

The [verification index](evidence/verification.md) routes to existing evidence for
published version 0.3.4. The [FW00 packet](evidence/fw00-verification-index-20261013/README.md)
owns this docs-only change, its source ledger, checks and remaining gates.

Completed in the earlier source/publication wave: the [release packet](evidence/releases/2026-10-13-member-gates/README.md#published-readback)
records the original tag, successful run and package readback. This navigation
change does not rerun those historical events or assert installed/native quality.

Exact next task: integrate the frozen docs-only candidate through genuine required
checks and normal merge. Independent navigation/payload review and the owner's
local command set passed; the [subsequent gate receipt](evidence/fw00-verification-index-20261013/owner-gates.json)
preserves their exact sources. A successor containing only these receipts receives
final structural, link and package-conservation checks before promotion. No new
version, tag, publication, provider call or host-profile update belongs here.
