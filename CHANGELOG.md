# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project uses
[semantic versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] — 2026-09-20

### Added

- **`quest-spatial`** — the Kotlin lane. Meta Spatial SDK is how an Android team
  reaches Horizon OS, and the pack had no answer for it: which lane it is right
  for, the toolchain it demands (Horizon OS v69+, AGP 8.11.1 under the Gradle
  9.4.1 wrapper, Kotlin 2.1.0, JDK 17, Spatial Editor for all but two samples),
  and the budgets that decide a design rather than tune it — 2,000 entity
  operations per tick, 500 physics objects, ~1,000 scene-graph entities, and a
  panel table whose sharpest rows are three video panels and two activity-based
  ones.
- Its three references: `samples-map.md` (15 official samples mapped to the
  question each answers, plus the `hzdb` MCP server a clone brings with it),
  `docs-map.md` (197 pages, by prefix and by topic), `budgets-and-traps.md`
  (the tables, and the five issues Meta lists against itself — including debug
  builds being slow enough to invalidate a measurement, and `finish()` on an
  immersive activity crashing inside `libMetaSpatialSDK.so`).

### Changed

- The pack now routes six lanes, not five; Meta's `hz-spatial-sdk` still owns
  the implementation of a Spatial SDK app, and `quest-spatial` says when to be
  there at all and where to read.

## [0.1.5] — 2026-09-20

### Fixed

- `test/social_preview.py`, the last CI step this repository inherited a job for
  and never inherited the script for. Every step of both jobs has now been run
  locally against this tree before the push, which is how the previous two
  failures should have been caught.

## [0.1.4] — 2026-09-20

### Fixed

- CI was red on the first push and the repository did not know it: the online
  schema check imports `SCHEMA_FOR` from the validator, which exported only an
  internal `SCHEMAS` map, and the audit job ran a `test/evals_validate.py` that
  had never been copied in. Both closed — the pinned addresses now live in one
  map that both halves read, and the eval data validates with its own planted
  defect.

### Added

- `test/evals/README.md` and `RESULTS.md`. Results says, in as many words, that
  no model run has happened yet: an unrun eval reported as a pass is worse than
  no eval.
- The trigger split now carries **both classes in each half** — a train split of
  positives only cannot show over-firing, which is the failure mode that matters
  beside Meta's 29 neighbouring skills.

## [0.1.3] — 2026-09-20

### Added

- `docs/assets/social-preview.png` — the card the family umbrella generates for
  this member from `skills.json`, byte-compared in its suite so the pixels and
  the manifest cannot drift apart.

## [0.1.2] — 2026-09-20

### Added

- `docs/AGENT_SYNC.md`, generated from the live coordination config, and a
  repository `CLAUDE.md` that links it and states the invariants each gate
  checks. A guarded-file list no agent instruction points at is a list nobody
  reads.

## [0.1.1] — 2026-09-20

### Changed

- `quest-tooling`'s description trimmed back inside the 60-character reserve the
  family keeps below the 970 cap — the room a near-miss neighbour's "NOT for"
  clause will need.
- README says where its verification commands run: a clone, not the published
  package, which ships the skills without `test/`.

### Added

- `.claude/agent-sync.json`, so a second agent in this repository claims the
  guarded files instead of overwriting them.

## [0.1.0] — 2026-09-20

First release. Five skills, seven references.

### Added

- `quest-native` — the native OpenXR lane: development versus release manifest,
  SDK levels including the 1 March 2026 target-34 rule, the Khronos loader and
  its two initialisation extensions, the frame loop and the focus rules review
  enforces, capability checks over device models.
- `quest-perf` — per-refresh-rate frame budgets, the `GPU%` reading that falls
  exactly when an app is GPU-bound and the 50% threshold behind it, the four
  recovery levers in order, and a capture playbook for Perfetto, simpleperf,
  RenderDoc and OVR Metrics through `metavr`.
- `quest-tooling` — the metavr CLI surface, its MCP server and how one server
  ends up registered twice, `metavr init`'s all-agents default measured at 4129
  files inside a repository, the managed tool matrix, and the hygiene rules.
- `quest-store` — the four release channels and what review actually checks,
  the VRC list generated from Meta's page (80 requirements, 14 groups), the
  release manifest delta, uploading with `metavr store dist`.
- `quest-webxr` — requesting an immersive session on load, IWSDK versus three.js
  versus A-Frame, Bubblewrap packaging with the Digital Asset Links step, and
  the performance honesty a browser build needs.

[0.2.0]: https://github.com/ssheleg/xr-dev/releases/tag/v0.2.0
[0.1.5]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.5
[0.1.4]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.4
[0.1.3]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.3
[0.1.2]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.2
[0.1.1]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.1
[0.1.0]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.0
