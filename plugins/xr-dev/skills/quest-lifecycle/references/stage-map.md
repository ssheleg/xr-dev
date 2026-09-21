# Stage map and product evidence

**Read this when**: a full plan, inherited project or pre-launch audit. The stages below are
platform work inside the project's existing delivery process. Read on 2026-09-21;
this is an authored workflow, not an assertion that Meta prescribes these files.

| Stage | Agent proposes without waiting to be prompted | Owner and evidence gate |
|---|---|---|
| Discovery | Identify audience, repeatable core experience, target devices, app category, engine, distribution and operating cost | Product/UX + engine owner: target contract and smallest risky spike |
| Account and policy preparation | Team/organization verification, roles, commercial account if paid, age audience, data flows and feature eligibility | quest-store: actual Dashboard tasks/status and owner; private documents stay private |
| Spatial prototype | Comfortable first use, seated/standing and room variations, controls, tracking/permission failures, onboarding | UX + immersive designer: tested scenarios and user feedback; no comfort proof from desktop |
| Technical vertical slice | Reproducible build, input, asset import, lifecycle/save path, real-device instrumentation | engine owner + quest-tooling: build SHA and device capture; offline/error paths |
| Production | Content/quality budgets, performance experiments, dependency updates, localization, multiplayer/service costs | quest-perf + engine: representative sustained scenes, CPU/GPU/memory evidence |
| Audience and capture | Positioning, Coming Soon eligibility, capture build/shot list, layered key art, press kit, owned community | quest-store + copywriting/design/Foundry: truthful assets tied to source builds and rights |
| Monetization | Compare business models, pricing/regions, IAP/subscription/entitlement backend, support/refunds | quest-store + product owner: test-account purchases, renewal/cancel/restore/failure evidence |
| Release candidate | VRC applicability, merged manifest/signature, privacy/rating, reviewer instructions, device matrix | quest-store: per-requirement evidence, account tasks and exact candidate identity |
| Submission and launch | Review buffer, response owner, launch schedule, customer support, backend readiness, launch verification | release owner: submission/approval/build records and real customer-path checks |
| Operate and improve | Crash/ANR, latency/frames, sessions/retention, funnel/revenue, refunds/support, content updates and deadlines | operations: dated metric definitions and corrective next action; rehearsed compatible recovery |

Recommended records: `docs/xr/source-ledger.md` for claim/source/applicability;
`docs/xr/release-readiness.md` for gate/status/evidence; `docs/xr/launch-plan.md`
for audience, promise, channel, asset, owner, date, budget, metric and contingency.
Do not put account secrets, tax documents or individual tester data in public Git.

## Discovery prompts are prompts for the agent

Inspect answers first. Ask the operator only what the repository cannot settle:
who it serves; where and how long it is used; acceptable input/comfort modes;
lowest supported hardware; online dependency; commercial model; launch constraint.
Separate a decision needed now from a later experiment. Recommend a default with
its tradeoff instead of making the operator learn an SDK vocabulary.

For inherited projects, audit each stage against what exists. Do not restart a
working project or migrate engines to match this map. Recover missing evidence
with the smallest representative build, then proceed from the earliest blocker.

## Gates that often disappear between owners

- Feature support, Android permission, Meta data access/account approval and
  runtime tracking availability are different gates.
- Build review, Store assets, age/content rating, commercial setup and data
  assessments do not become complete together. DPA applies when the Dashboard
  requires it; do not equate every project with an annual assessment task.
- Multiplayer needs matchmaking/session transport, ownership, reconnection and
  moderation where applicable; a shared anchor only aligns coordinates.
- Capture/marketing needs real gameplay provenance and separate consent/licensing;
  a generated concept image cannot stand in for a required gameplay screenshot.
- Release recovery must respect signing identity, increasing Android versionCode,
  save-schema compatibility, backend protocol and product entitlements. Test a
  forward recovery build; do not promise that uploading an old APK is rollback.
- Test-device success does not prove a non-team user can buy, launch, restore or
  receive updates. Record what could and could not be tested before launch.

## Primary navigation

- [Learning path](https://developers.meta.com/horizon/resources/developer-learning-path/): dependencies across design/development/distribution.
- [Launch](https://developers.meta.com/horizon/resources/launch-your-app/): launch preparation and sequence.
- [Submit](https://developers.meta.com/horizon/resources/publish-submit/): application categories, submission and suggested review buffer.
- [DPA](https://developers.meta.com/horizon/resources/publish-data-protection-assessment/): applicability and actual Dashboard tasks.
- [Organization](https://developers.meta.com/horizon/resources/publish-organization-verification/): account prerequisite.
