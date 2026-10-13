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
| GATE-05: align full-check scheduling with operator policy | 23:00 Europe/Warsaw schedule, workflow_call and explicit-candidate dispatch with recorded reason; no push/automatic PR update triggers; ready_for_review only |

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
exact-SHA review, then move the pushed draft candidate to ready once for genuine required checks. Native/model behavior,
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

- `test/member_gates.py`: `6d297aa8fe285e5aaaad67357829315e78ee014eb38ae6deec3d0753c8b94ff0`.
- `test/member_gates_test.py`: `b3ef7e6dc667f6b26b481c108443fdf1b6945a9133ab488a75b7fcd2e99c89e0`.

## Hosted validation scope

Validation now has `schedule` at 23:00 Europe/Warsaw, `workflow_call` for release,
and `workflow_dispatch` with required `candidate_reason`. Push and automatic PR opened/synchronize triggers were removed under the
coordinator's explicit instruction; ready_for_review is the only PR event. The workflow parsed with
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


## Review correction and final bounded contract

Self-review reproduced an accepted duplicate release job and successful exit
before ancestry, then a successful exit inside the refusal branch. Independent
review by the hub coordinator reproduced quoted mapping keys overriding release,
run, fetch-depth and steps; a Row table silently escaped declaration uniqueness;
and missing/late Markdown separators passed. These accepting cases preceded
the corresponding correction. The first shell-override regression was also red
(26 process controls, 1 failure) before the step-leading shell property was fixed.

A final merge-key plant (`<<: {continue-on-error: true}`) initially survived
the real validator: 42 process controls, one failure. Merge keys now fail closed
before structural inspection.

The final common helper requires ID declaration tables and their immediate,
matching Markdown separator. Row reference ledgers are explicitly unsupported
in these new boards; they are not silently treated as declarations or ignored.
It reads each table's own width and rejects duplicate IDs across declarations.

Release validation is intentionally bounded to the current plain mapping keys,
two-space jobs and six-space steps. Quoted keys, YAML merge keys, duplicate jobs/steps/run/checkout
options and depths, unknown defaults, conditional or ignored ancestry, and
nonstandard shell setup fail closed. The supported setup is set-eu, resolve the
actual default branch, fetch it, then the ancestry condition; the refusal branch
permits diagnostic echo commands followed by exit 1. This is a maintainable
structural contract, not a general YAML parser or arbitrary shell verifier.
Changing that grammar requires explicit review and new controls. Valid escaped
pipes, bold/linked IDs, differing table widths and explicit false failure-ignore
flags remain accepted.

The final harness has **42 process controls: 38 hostile plants and four valid
controls**. All copies use the same helper and harness bytes. The last local
command results are recorded below; older 18/19/26-control results above are
intermediate observations, not the final result.

## Final candidate CI policy

Only `pull_request.types: [ready_for_review]` triggers a candidate suite. The PR
is created as draft, independently reviewed and locally gated, then moved to
ready once at its frozen head. No push/opened/reopened/synchronize trigger was
added. The 23:00 Europe/Warsaw schedule and release workflow_call remain.
workflow_dispatch with required candidate_reason is retained only for standalone
diagnostics; it does not satisfy PR required checks. This corrects the earlier
candidate-dispatch design above. Job bodies are unchanged.

GitHub's [required-check event contract](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks#checks-from-some-workflow-jobs-are-not-evaluated),
read 2026-10-13, explicitly excludes workflow_dispatch jobs from PR admission.
The coordinator verified that behavior during this wave. A check must be a real
eligible-event job at the candidate head or its matching test merge commit;
there is no synthetic status, branch-protection bypass or release authorization.

## Final local receipt

`npm test && npm run test:negatives && git diff --check` completed with
exit 0 after the merge-key correction, sequentially across the three members.
The negative gate refused 8 original defects and passed all 42 common
process controls (38 hostile plants, four valid controls). Workflow parsing
assertions also passed: exactly four events, ready_for_review only for PRs,
23:00 Europe/Warsaw, required candidate_reason, and job bodies equal to the
canonical-main baseline. Earlier installer and strict-manifest checks above
remain applicable: these files did not change during parser review.

Final source SHA-256:

- `test/member_gates.py`: `6d297aa8fe285e5aaaad67357829315e78ee014eb38ae6deec3d0753c8b94ff0`.
- `test/member_gates_test.py`: `b3ef7e6dc667f6b26b481c108443fdf1b6945a9133ab488a75b7fcd2e99c89e0`.

Independent final-commit approval and hosted PR admission remain pending at
this source receipt. Next: verify this exact commit, create or retain a draft
PR, then promote the frozen candidate once and watch the genuine check jobs.
No merge, release or hub pin update is authorized by this receipt.
