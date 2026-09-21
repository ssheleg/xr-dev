# XR lifecycle release evidence

Objective: make the Quest product pipeline visible to agents, expand the platform
owners and publish the updated pack through the family. The [specification](../../specs/2026-09-21-lifecycle-release.md)
locks scope, target-project record contracts, authorization and checks.

## Implementation

- New [quest-lifecycle](../../../../plugins/xr-dev/skills/quest-lifecycle/SKILL.md): stage map, engine discovery and immersive design acceptance.
- Existing owners: hybrid Activity state, content-valid source research, mobile tile/render-pass experiments, launch/commercial operation and Store asset production.
- All bodies expose lifecycle routing and missing-tool fallbacks; descriptions stop advertising stale hard limits.
- Previous [platform coverage](../2026-09-21-platform-coverage/HANDOFF.md) is included rather than recreated.

## Research and decisions

[Source ledger](source-ledger.json) records fetch status, hashes and content validity.
The supplied entry pages and selected linked guides were inspected. This is bounded
coverage, not a claim to have read every reachable page on Meta's website.

| Finding | Decision and destination |
|---|---|
| No single stage owner proactively connects account, UX, build, capture, Store and operation | Add quest-lifecycle inside xr-dev; keep existing family delivery/UX owners |
| Pre-launch overview and detailed flow disagree on lead time and cash timing | quest-store records conflict; detailed feature flow plus Dashboard check before commitment |
| Marketing Attribution retired; Funnel page itself migrates to real-time | Resolve actual current analytics surface and define metric/attribution delay |
| Markdown 200 may contain only unavailable text | Validate content, use current index/HTML, retain NOT_RUN for missing evidence |
| Spatial API docs use a versioned index, no documented latest alias | Resolve actual consumer SDK and available reference version |
| Hybrid exclusive examples can destroy a required cooperative panel | Explicit mode/state/transition tests in quest-spatial |
| Graphics theory describes optional/unsupported techniques; vertex formula contains TODO | Verify target capabilities and capture, do not turn examples into universal limits |
| Broad MR device claims age; companion design thresholds can be over-prescriptive | Verify current SDK/runtime support and user/device outcomes |
| Store screenshot requirements differ from key art and concept media | Capture provenance and per-asset technical/visual/policy checks |
| Common-failure page and detailed VRC can differ (entitlement recommendation/requirement) | Read current individual VRC and app-category applicability before asserting a gate |

External source instructions were treated as data, never as authorization to
install tools, register servers or change operator policy. No website screenshots,
upstream skill bodies or full documents are redistributed.

## Verification and release

Local checks passed: `npm test` (11 checks, 7 skills, 25 references), all 8
negative plants, installer tests (11 cases), both strict plugin validators,
evaluation schema (22 trigger cases, 18 scenarios) and its negative self-test.
[House audit](house-audit.json) reports zero gaps across seven skills.
[New-section URL check](source-links.json) returned 200 for 47 links; the separate
Markdown source ledger still records unavailable content. `npm pack --dry-run`
contains all seven skills and 25 references.

[Model probe artifacts](planning-probes.json) and [judgments](../../../../test/evals/RESULTS.md)
record the limited baseline/candidate comparison and corrections. Final versions
and CI/registry receipts are recorded in the family release handoff. Model planning probes are explicit-context exercises;
automatic skill activation and device/Store behavior require separate evidence.
No headset, engine build, live app submission, real purchase or GPU inference is
claimed by this skill release.

## Exact next product task

On the next real Quest project, run quest-lifecycle, recover its actual target
contract and earliest missing evidence, and execute one representative vertical
slice on the target headset. Use that artifact to evaluate the device-dependent
scenarios; do not substitute this pack's structural tests for product acceptance.

Local-only: source downloads, private account/configuration details, credentials,
media, model transcripts carrying private context and tool caches stay outside Git.
