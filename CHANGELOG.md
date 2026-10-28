## v0.4.5: quest-store and quest-tooling advertise forms that name the headset

- **quest-store and quest-tooling advertise forms that name the headset** (hub board row B-298):
  their generic store and Android words ("release channel", "test user", "developer mode",
  "install the APK", "симулятор") route nowhere in the hub, because every mobile app uses them.
  The `## Triggers` sections now also carry qualified forms ("Quest release channel", "Horizon
  Store review", "Quest developer mode", "Meta XR Simulator" and their Russian pairs) that the hub
  can route without speaking for phone apps. Descriptions are unchanged.

# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project uses
[semantic versioning](https://semver.org/spec/v2.0.0.html).

## v0.4.4: descriptions within a 300-character budget

- Every skill description now fits a budget of about 300 characters (hub board row B-255 (a)):
  Claude Code lists every installed skill's description each session against a shared budget of
  about 30,000 characters, and the operator's listing measured 51,178, so less-used skills lost
  their descriptions. Measured with whitespace collapsed: `quest-lifecycle` 415 → 299,
  `quest-native` 456 → 296, `quest-perf` 443 → 292, `quest-spatial` 443 → 297, `quest-store` 453 →
  299, `quest-tooling` 423 → 297, `quest-webxr` 443 → 292; total 3076 → 2072.
- Each description keeps its router sentence, its boundary against sibling skills, the opt-out
  phrase and a short English and Russian trigger list. Every quoted trigger the description
  dropped is kept in the body's `## Triggers` section, so the family hook's words stay advertised
  (`test/advertised_check.js` in the hub).

## v0.4.3: the family member gate

- `test/family_gate.py`, the family's canonical member gate (hub B-108, B-109): the board
  parses (every row as wide as its header, no id twice) and `release.yml` keeps the tag-ancestry
  check (`fetch-depth: 0`, `git merge-base --is-ancestor`), each watched failing on a plant by
  `--self-test`. Wired into `npm test`; a byte-for-byte copy of the hub's `member-gate/family_gate.py`.

## v0.4.2: the ledger records the shipped version

- The verification ledger records this version: 0.4.1 shipped with the ledger still headed by the version before it. No skill changes.

## v0.4.1: no private project or service names

- `quest-native` named one of the operator's private projects in its lock-file example and a private media service in the project playbook. Both are now neutral ("one Quest project", "the configured asset/job owner"). No behaviour changes.

## 0.4.0 (2026-10-20)

- Every skill's front-matter `description` is now a router, not a manual: one
  "Use when" sentence, a "NOT for" boundary naming the sibling skill, the opt-out
  phrase (no xr, без xr) and a few English and Russian triggers. Lengths before and
  after: quest-perf 901 to 443, quest-tooling 885 to 423, quest-spatial 882 to 443,
  quest-native 855 to 456, quest-webxr 850 to 443, quest-store 788 to 453,
  quest-lifecycle 726 to 415 (5,887 to 3,076 chars in total).
- Why: Claude Code shares about 30,000 chars of skill listing across every installed
  skill. Measured on 2026-10-20, the operator's listing held 29,995 chars for 134 skills
  and 81 of them showed no description. Plugin skills cannot be hidden, so description
  length is the only lever.
- Every trigger phrase removed from a description moved verbatim (EN/RU pairs kept
  together) into a new `## Triggers` section at the end of that skill's body, so the
  family's routing hook still finds each of its words in the skill's text.
- `test/validate.py`: the house description cap drops from 970 to the family cap of
  500 chars; the standard's 1024 stays the hard limit. `CLAUDE.md` states the new rule.

## 0.3.4 — 2026-10-13

- Validate the owner board's table shape, unique task IDs and immediate Markdown
  separator before accepting a change.
- Validate the release job's full-history checkout and refusing ancestry check;
  reject unsupported or ambiguous workflow shapes. Forty-two process controls
  cover hostile edits and valid board/workflow forms.
- Run complete hosted validation nightly at 23:00 Europe/Warsaw or once for an
  explicitly frozen draft-to-ready candidate. Tag releases retain their existing
  validation and publication checks.

## 0.3.3 — 2026-10-10

- **The release refuses a lightweight tag.** `release.yml` gains one step, right after
  checkout and before any gate: `git cat-file -t` on the tag must print `tag`; a `commit`
  fails the job with the remedy (`git tag -a <tag> -m '<release>'` at the same commit)
  before anything is published. `git describe` and `git submodule status` see annotated
  tags only, and the 2026-10-09 family wave cut four lightweight member tags that the
  umbrella then read as each member's previous release. The step is identical across the
  family (umbrella plan 2026-10-10, T5 / REQ-6). Published tags are not re-cut.
- No skill, reference or installer change.

## 0.3.2 — 2026-09-27

- `quest-webxr` names its new neighbour: three.js scene, asset and animation depth off the
  headset belongs to `web3d-dev` (renderer and TSL, the glTF pipeline, the animation
  protocol). The Quest session, frame budget and packaging stay here. Description 779 → 850
  of 970 characters.
- `SKILL-CARD.md` stated version `0.1.0` through three releases; it now matches.

## 0.3.1 — 2026-09-21

- Make GitHub OIDC the explicit npm publishing path, without a stored npm token.
- Normalize npm repository metadata and document tag-triggered releases, initial trust setup and recovery.

## 0.3.0 — 2026-09-21

- Add quest-lifecycle: a portable product-stage map with proactive next actions, engine selection, immersive-design acceptance and evidence gates.
- Extend all six existing owners with platform/research/rendering coverage, cooperative hybrid activities, source-conflict handling, commercial readiness, capture and Store asset production, and post-launch analytics.
- Correct stale descriptions, hard Spatial limits, CPU/GPU timing claims, release manifest guidance and duplicate MCP setup defaults. Keep current SDK/device/Dashboard checks explicit.
- Add lifecycle evaluation cases and record isolated baseline/candidate planning probes separately from routing, build and headset verification.


## [0.2.1] — 2026-09-20

### Changed

- `quest-spatial`'s description trimmed to 882 characters. It shipped at 955 and
  moved the family's reserve ratchet — the 60 characters below the 970 cap exist
  for the "NOT for" clause the next neighbouring skill will force, and this pack
  now sits beside Meta's `hz-spatial-sdk`, which is exactly such a neighbour.
- The card the umbrella generates for this member, regenerated from the new
  manifest.

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

[0.2.1]: https://github.com/ssheleg/xr-dev/releases/tag/v0.2.1
[0.2.0]: https://github.com/ssheleg/xr-dev/releases/tag/v0.2.0
[0.1.5]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.5
[0.1.4]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.4
[0.1.3]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.3
[0.1.2]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.2
[0.1.1]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.1
[0.1.0]: https://github.com/ssheleg/xr-dev/releases/tag/v0.1.0
