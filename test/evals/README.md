# Evaluations for xr-dev

These files describe behaviour to measure with the pack installed. They are not
unit tests, and CI does not pretend that schema validity is model quality.

| File | Holds |
|---|---|
| `triggers.json` | 14 requests — positives and close negatives — split train/validation before any tuning |
| `scenarios.json` | 5 end-to-end behaviours, scored line by line |
| `RESULTS.md` | dated model runs, or an explicit statement that none exist |

Each case is written against a **failure observed without the pack** on
2026-09-20; the baseline table is in `docs/evidence/specs/xr-dev-0.1.0.md`.

Validate the data, and watch the validator refuse its own planted defect:

```bash
python3 test/evals_validate.py
python3 test/evals_validate.py --self-test
```

To measure triggers, ask each query in a fresh session three times and record
whether the intended skill loaded. To measure scenarios, record each expected
line as pass or fail. Always record the model, the pack version and the other
installed skills — **coexistence changes routing**, and this pack ships next to
Meta's 29, which cover neighbouring ground on purpose.

The negatives matter more than the positives here. `q12` (a Unity script) must
**not** fire a skill in this pack: Unity is Meta's lane, and a pack that answers
there is the duplication this one was built to avoid.
