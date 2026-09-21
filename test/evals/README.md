# Evaluations for xr-dev

`triggers.json` defines selection positives and close negatives; `scenarios.json`
defines expected behavior. Run `python3 test/evals_validate.py` for computed counts
and `python3 test/evals_validate.py --self-test` to verify rejection of malformed
input. Schema validity is not model quality.

Original cases trace to `docs/evidence/specs/xr-dev-0.1.0.md`; platform coverage
additions trace to `docs/evidence/specs/2026-09-21-platform-coverage.md`; lifecycle
cases trace to `docs/evidence/specs/2026-09-21-lifecycle-release.md`. Do not claim
all cases share a historical baseline. `RESULTS.md` records executed evidence.

For runtime selection, use fresh sessions and record the host/model, plugin/skill
versions and actual neighboring descriptions. Repeat each query three times;
judge selection separately from answer correctness. A Unity-only script bug must
not load the whole lifecycle workflow; a multi-stage Quest launch should.

Isolated explicit-context planning probes exercise artifact correctness only.
They do not prove automatic skill activation, tool calls, engine builds, actual
Dashboard eligibility, comfort, thermal performance or a customer purchase.
