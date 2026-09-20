# Evaluation results

**Status: authored 2026-09-20, never executed.** No model run has been recorded
against this pack yet. The table below is empty on purpose — CI proves the
shape of the eval data, not the behaviour of any model, and an unrun eval
reported as a pass is worse than no eval at all.

| Date | Version | Model | Trigger pass rate (train / validation) | Scenario lines passed | Installed alongside | Notes |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | not yet run |

## Method, when it is run

1. Fresh session per query, three repetitions, nothing else in the prompt.
2. Record which skill loaded, not whether the answer sounded right.
3. Record the full installed set: this pack is designed to coexist with Meta's
   `meta-vr@meta-quest` (29 skills), and routing is measured **with** it
   installed, because that is the machine the pack ships onto.
4. Score scenario lines independently; a scenario is not a single verdict.
5. Record the model and the pack version in the row, then leave the row alone —
   a re-run is a new row, never an edit.
