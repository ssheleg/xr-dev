# xr-dev — Meta Quest product lifecycle, seven skills

Agent skills for taking Quest games and apps from platform choice to release and
operation. Each stage names its owner, evidence and next action, so the agent can
surface account, design, performance and launch work before it becomes a blocker.

Part of the [ssheleg harness](https://skills.sshlg.me/harness/). This pack works
independently and composes with the family delivery, UX and design skills.

## The seven skills

| Skill | Answers |
|---|---|
| [quest-lifecycle](plugins/xr-dev/skills/quest-lifecycle/SKILL.md) | What stage is this product at, what is missing, and what should happen next? |
| [quest-native](plugins/xr-dev/skills/quest-native/SKILL.md) | How is the C/C++ OpenXR project built and audited, including MR capability and lifecycle boundaries? |
| [quest-spatial](plugins/xr-dev/skills/quest-spatial/SKILL.md) | How do Kotlin Spatial SDK, ECS, panels and hybrid activities fit this app? |
| [quest-perf](plugins/xr-dev/skills/quest-perf/SKILL.md) | What limits frames, memory or sustained performance, and which rendering experiment tests it? |
| [quest-tooling](plugins/xr-dev/skills/quest-tooling/SKILL.md) | Which tools and sources are available, current and appropriate for this host? |
| [quest-store](plugins/xr-dev/skills/quest-store/SKILL.md) | What remains for testing, submission, monetization, Store assets, launch and operation? |
| [quest-webxr](plugins/xr-dev/skills/quest-webxr/SKILL.md) | How does the browser/PWA experience handle sessions, optional features and delivery? |

References live inside their owning skill and load on demand. The skill bodies
link every shipped reference with a use condition. For the complete change and
verification record, see [lifecycle release evidence](docs/evidence/verification/2026-09-21-lifecycle/README.md).

## Start with the product stage

For a new or inherited product, invoke `/quest-lifecycle` from a skills directory
or `/xr-dev:quest-lifecycle` from the plugin. It inspects the actual engine and app
category, preserves existing project records, and proposes the earliest unresolved
step. For a single bug, capture or upload, use that specialist directly.

The workflow covers platform selection, immersive UX, a device-tested vertical
slice, content/performance budgets, commercial prerequisites, real gameplay
capture, Store review and post-launch checks. It distinguishes 2D, immersive,
hybrid, WebXR, packaged PWA and PC VR requirements.

[Meta's own companion skills](https://github.com/meta-quest/agentic-tools) supply
engine and tool workflows when installed. The lifecycle engine map also points
to Godot's official XR/export/vendor-plugin documentation. This pack supplies
fallback procedures; it does not install an engine, promise every device feature,
or treat a generated image as gameplay evidence.

## Install

Claude Code plugin:

```text
/plugin marketplace add ssheleg/xr-dev
/plugin install xr-dev@xr-dev
```

Portable Agent Skills:

```bash
npx skills add ssheleg/xr-dev
```

The standalone npm installer also works when the same Claude plugin is absent:

```bash
npx @ssheleg/xr-dev --help
```

Use one channel per agent. For a composing family installation, update through
`npx sshlg-skills update`. Restart the agent after updates so skills reload.

## Tools and source freshness

Inspect existing CLI/MCP/plugin registration before setup. `quest-tooling` maps
Meta VR CLI, device/debug/profiling tools and Markdown documentation indexes,
with the operator's gateway policy taking precedence over generic setup examples.
No MCP uses CLI; no CLI uses official docs; absent engine/device/account access
leaves dependent checks explicitly unverified. An HTTP 200 may be an unavailable
page, and a source example is not a universal SDK or Store requirement.

## Verifying a change

<!-- commands-run-in: a clone -->
The repository carries tests; the npm payload carries the skills and references.

```bash
npm test
npm run test:negatives
node test/installer_test.js
python3 test/evals_validate.py
claude plugin validate . --strict
claude plugin validate plugins/xr-dev --strict
```

[Test evaluation documentation](test/evals/README.md) separates scenario definitions,
isolated model planning probes, runtime routing and device/product evidence.

## Releases

Push a `vX.Y.Z` tag after its versioned commit reaches the default branch. GitHub
Actions validates the pack, creates the GitHub release and publishes to npm with
provenance through trusted publishing. Ordinary branch pushes run checks only.
See [release setup and recovery](docs/RELEASING.md).

## License

MIT for this pack. Primary documentation is linked and dated; third-party tools,
assets and models retain their own licenses. Recheck volatile requirements before
implementation and submission.
