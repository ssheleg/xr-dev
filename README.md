# xr-dev — Meta Quest and Horizon OS, six skills

Agent skills for building, profiling and shipping XR on Meta Quest. They answer
the questions that sit *above* a tool: which build lane a project is on, which
number in a capture is the real one, what the Store will reject, and where the
authoritative answer lives.

Meta publishes [29 task skills of its own](https://github.com/meta-quest/agentic-tools)
— twelve of them Unity-specific. **This pack does not duplicate them.** It owns
the native OpenXR lane, the measurement, the toolchain hygiene and the release
seam, and routes to Meta's skills where they own the tool.

## The six skills

| Skill | Answers |
|---|---|
| `quest-native` | a native OpenXR app in C/C++: the two manifests, the Khronos loader, the frame loop, SDK levels |
| `quest-spatial` | the Kotlin lane — Meta Spatial SDK: toolchain versions, ECS, the panel budgets that decide a design, and 15 samples mapped to what each one answers |
| `quest-perf` | the frame budget, why `GPU%` reads low exactly when an app is GPU-bound, and how to capture |
| `quest-tooling` | the metavr CLI and its MCP server, the managed tools, and one install channel per agent |
| `quest-store` | the four release channels, the VRC list, the release manifest, uploading |
| `quest-webxr` | WebXR sessions, IWSDK, Bubblewrap packaging and the asset-links step that decides whether a PWA launches |

Each ships its references, loaded on demand:

- `quest-native/references/` — `manifest-and-gradle.md`, `frame-loop.md`, `doc-map.md`
- `quest-spatial/references/` — `samples-map.md`, `docs-map.md`, `budgets-and-traps.md`
- `quest-perf/references/capture-playbook.md`
- `quest-tooling/references/tool-matrix.md`
- `quest-store/references/vrc-checklist.md` (80 requirements across 14 groups, generated from Meta's page)
- `quest-webxr/references/pwa-packaging.md`

## What is inside that is hard to find elsewhere

- **The GPU% trap.** At half rate a GPU-bound app reports ~65% utilisation.
  `App` in milliseconds against the refresh-rate budget is the number that is
  true; utilisation must fall below ~50% at half rate before full rate returns.
- **Two manifests, one of them enforced.** Development and release requirements
  are different documents; only the release set is checked at review.
- **`targetSdkVersion` 34 since 1 March 2026** for new apps — and a lock file
  that still says 32 is a release note for a build that does not exist.
- **`metavr init` with no target flag means every agent it knows**, into the
  current directory: measured at 29 skills × 25 directories = 4129 files, 47 MB,
  inside a game repository, committed by the next `git add -A`.
- **An alpha build is not exempt from packaging requirements**, and the
  Production channel is the only one that triggers review.
- **Spatial SDK's budgets are the shape of the design, not tuning advice**:
  three video panels, two activity-based panels, 2,000 entity operations per
  tick, ~1,000 scene-graph entities, +480,000 panel pixels ≈ +1% GPU.
- **AGP 8.5 or earlier under the Gradle 9 wrapper fails during CMake model
  sync** — the error blames CMake and the fix is AGP 8.11.1.
- **Every Meta doc page has a Markdown twin** at
  `developers.meta.com/horizon/llmstxt/<path>.md` — no scraping, no login.

## Install

Claude Code (plugin — the channel that updates):

```
/plugin marketplace add ssheleg/xr-dev
/plugin install xr-dev@xr-dev
```

Any of 70+ agents, through the skills CLI:

```bash
npx skills add ssheleg/xr-dev
```

Plain copies into `~/.claude/skills/` (only when the plugin is *not* installed —
a copy shadows it and serves its frozen version forever):

```bash
npx @ssheleg/xr-dev            # --force to overwrite, --help for the exit codes
```

Skills load at session start: **restart the agent** after installing.

## Companion tooling

The skills assume, and degrade without, the Meta VR CLI:

```bash
curl -fsSL https://developers.meta.com/horizon/install-cli/ | sh
metavr auth login && metavr doctor
```

No `metavr`, no MCP server and no headset still leaves every skill useful: each
one names the documentation address to fetch by hand and says which steps need
hardware.

## Verifying a change

<!-- commands-run-in: a clone -->
From a clone of this repository — the published package ships the skills, not
the test suite:

```bash
npm test               # the house validator: structure, budgets, references, links
npm run test:negatives # plants each defect and fails if a guard stays green
node test/installer_test.js
claude plugin validate . --strict && claude plugin validate plugins/xr-dev --strict
```

## License

MIT. Documentation facts are quoted from Meta's developer documentation with
the date they were read; re-verify before quoting them onward.
