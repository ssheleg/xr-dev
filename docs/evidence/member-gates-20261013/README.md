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

Implementation and local gates are complete. Next: obtain an independent
exact-SHA review, then push a frozen candidate for coordinator integration. Native/model behavior,
provider tests, release, installation and hub pin updates are NOT_RUN here.
Source request: [hub B-108/B-109](https://github.com/ssheleg/sshlg-skills/blob/ab377787/docs/evidence/backlog.md).


## Observed verification

- Before implementation, `python3 test/member_gates_test.py` against the original
  owner validator reported **19 controls, 16 failures**, exit 1: every hostile
  plant survived and all three valid controls passed. Each temporary copy was
  owned by this harness and removed before the next case.
- `npm test`: exit 0, structural validator **12 checks**.
- `npm run test:negatives`: exit 0, **8 original defects** refused and
  **19 new process controls, 0 failures**. These invoke the actual member
  validator with clean baselines and changed-byte checks for each plant.
- `node test/installer_test.js`: exit 0, 11 cases; 11 scratch homes created and
  removed, no real home installation.
- `claude plugin validate . --strict` and
  `claude plugin validate plugins/xr-dev --strict`: both exit 0.
- `git diff --check`: exit 0.

The common helper and control harness are byte-identical in the three member
worktrees (SHA-256 observed):

- `test/member_gates.py`: `c519a300ea22e55eb0b9d70c68605e393c1f9949286bc8bdf8a676ee003e7193`.
- `test/member_gates_test.py`: `6d73a78dc33f0e3d98019282a7987458ddeba8dd45a98f1cf75d3eaa521a152a`.

## Hosted validation scope

Validation now has `schedule` at 23:00 Europe/Warsaw, `workflow_call` for release,
and `workflow_dispatch` with required `candidate_reason`. Push/PR triggers were
removed under the coordinator's explicit instruction. The workflow parsed with
PyYAML locally (exit 0), checking exactly these events, timezone and reason;
PyYAML is not introduced as an offline-gate dependency. The caller scan found
only `release.yml`; no Pages/deployment workflow triggers validation indirectly.
Release tags and the release job's dependency on validation remain unchanged.

GitHub documents [timezone schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
and [manual dispatch refs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow),
read 2026-10-13. Nightly checks cover the default branch, not this unmerged
candidate. A coordinator-approved explicit candidate run must be tied to its
actual head SHA and genuine job result. No full hosted run has been dispatched
at this local verification point; no required status was fabricated. No release,
native/device/provider acceptance or hub pin change is claimed.
