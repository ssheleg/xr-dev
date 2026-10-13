# xr-dev: member board and release gates

Objective: close the owner-side gaps described by the hub B-108/B-109 with
member-local, offline checks and witnessed negative plants. User authorization
is the 2026-10-13 autonomous family wave. Parent assigned this member explicitly.
No release, installation or hub pin update is in scope.

Canonical base: [ff0d06b3da0dc0149b930e84710ba538d175b62f](https://github.com/ssheleg/xr-dev/commit/ff0d06b3da0dc0149b930e84710ba538d175b62f).
Local main and other worktrees are preserved. Read CLAUDE.md, package.json,
.claude/agent-sync.json, docs/AGENT_SYNC.md, test/validate.py and both workflows.
The owner board is absent; the validator does not check board width/duplicates
or release fetch-depth/ancestry. The release workflow already has the runtime
ancestry guard; this work protects it in the member gate.

## Requirements and plan

| Requirement | Acceptance |
|---|---|
| GATE-01: create the owner board without fabricated historical closures | Rows cite current findings and this packet; width derives from each table header, IDs are unique |
| GATE-02: keep release ancestry and full-history checkout in the active job | Removal/comment/misplacement/disabled-step/ignored-failure plants are refused |
| GATE-03: prove the actual validator catches each defect | Run copied-tree subprocess controls before and after the implementation; prove the plant changed bytes and the clean control passed |
| GATE-04: keep the mechanism consistent across members | Byte-identical test/member_gates.py and test/member_gates_test.py from the Telegram pilot; only owner integration differs |
| GATE-05: align full-check scheduling with operator policy | 23:00 Europe/Warsaw schedule, workflow_call and explicit-candidate dispatch with recorded reason; no push/PR triggers |

Sequence: negative baseline on the unchanged owner validator; portable helper
and owner board; local full gates once; independent review; commit/push a frozen
candidate. If a required hosted status is needed, coordinator authorizes one
explicit candidate run and binds its actual head SHA. Never dispatch per push.
Inspect reusable-workflow callers first; do not change deployment semantics
merely to remove an indirect caller.

Task-pipeline owns delivery; make-skill the offline plugin gate; agent-sync local
advisory file ownership; evidence-docs the receipts. This test-only workflow
change has no product UX surface or provider call. The release guard is bounded
structural validation for the current workflow layout, not a general YAML/Bash
interpreter. No dependency is added to the member's stdlib-only offline gate.

## Resume

Next: record the observed negative baseline, apply the proven helper and run the
owner gates. Then obtain an independent exact-SHA review. Native/model behavior,
provider tests, release, installation and hub pin updates are NOT_RUN here.
Source request: [hub B-108/B-109](https://github.com/ssheleg/sshlg-skills/blob/ab377787/docs/evidence/backlog.md).
