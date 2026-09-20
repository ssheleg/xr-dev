# Spec — xr-dev 0.1.0

*Written 2026-09-20, before the skills. Baseline failures were observed the same
day in a live session on this estate, working on a native Quest project
(`elements-vr`) with Meta's own 29 skills installed and no pack of ours.*

## Contents

- The problem
- Baseline failures (measured, not imagined)
- Decisions
- Contract with target projects
- Out of scope

## The problem

Meta's agentic tools cover *tasks* (drive Perfetto, port a 2D app, retarget a
Unity avatar). Twelve of the twenty-nine are Unity-specific. Nothing covers the
questions that precede a tool: which lane a project is on, which number in a
capture is true, what the Store enforces versus recommends, and how the
toolchain should be installed so it does not end up inside the product.

## Baseline failures (measured, not imagined)

| # | Observed 2026-09-20 | Skill that answers it |
|---|---|---|
| B1 | `metavr init` run with its all-agents default inside a git repository wrote 29 skills × 25 directories — 4129 files, 47 MB — and commit `951174a` swept them into the product | `quest-tooling` |
| B2 | One MCP server registered twice (plugin + project scope): ~37 tool definitions duplicated in every session | `quest-tooling` |
| B3 | Two CLI installs (native 1.3.2.2.2 and npm 1.3.2) resolving by PATH order | `quest-tooling` |
| B4 | `dependencies.lock.json` said `targetSdk 32` while `build.gradle` said `34`; the release plan was written against the lock | `quest-native`, `quest-store` |
| B5 | Zero managed Meta tools installed on a machine doing Vulkan work with a Store plan — no Perfetto, no RenderDoc, no platform-utils | `quest-tooling` |
| B6 | Quest questions default to Unity answers when the project is native C++ | `quest-native` |
| B7 | `GPU%` read as headroom during frame drops — the documented trap, with no skill stating it | `quest-perf` |

## Decisions

1. **Five skills, split by the question, not by the tool.** A tool skill ages
   with the tool; a question skill ages with the platform.
2. **No Unity content.** Meta owns that lane with twelve skills; a second
   description of one API drifts and the stale one is indistinguishable.
3. **Every fact carries a read date and a re-verify instruction.** Horizon OS
   ships on its own cadence; a skill that freezes a number is worse than one
   that says where to look.
4. **The VRC reference is generated** from Meta's page, not transcribed: 80
   requirements across 14 groups, computed by the script that wrote the file.
5. **The machine-hygiene rules live in `quest-tooling`**, not in a README
   nobody loads: the failure they prevent (B1) happened to an agent, not a
   human.

## Contract with target projects

The pack reads, and never writes without being asked:

| Path | Read for |
|---|---|
| `**/AndroidManifest.xml` | manifest conformance, immersive vs 2D, categories |
| `**/build.gradle`, `*.lock.json` | SDK levels, loader version, ABI filters |
| `CMakeLists.txt`, `src/**` | which build lane the project is on |
| `.gitignore` | whether skill installs would land in the tree |

## Out of scope

Unity and Unreal authoring, visionOS and ARKit, PC-VR (Link) titles, 3D content
production, and the product decisions above the interface.
