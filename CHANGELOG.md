# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project uses
[semantic versioning](https://semver.org/spec/v2.0.0.html).

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

[0.1.3]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.3
[0.1.2]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.2
[0.1.1]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.1
[0.1.0]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.0
