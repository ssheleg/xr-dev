# Skill Card — xr-dev

## Identity

| Field | Value |
|---|---|
| Pack | `xr-dev` |
| Version | `0.1.0` |
| Skills | `quest-native`, `quest-perf`, `quest-tooling`, `quest-store`, `quest-webxr` |
| License | MIT |
| Source | https://github.com/ssheleg/xr-dev |

## Job and boundary

XR development on Meta Quest and Horizon OS: the native OpenXR lane, frame-budget
measurement, the toolchain on a development machine, Store distribution, and the
WebXR/PWA path. **Unity and Unreal work belongs to Meta's own skills** — this
pack routes there rather than duplicating them. Product decisions, visual design,
copy and payments keep their own owners.

## Inputs and outputs

Inputs: an existing XR project or an empty one, optionally a connected headset,
optionally the `metavr` CLI and its MCP server. Outputs: repository changes,
manifest and build configuration, capture reports with their evidence, and
submission checklists. Nothing is uploaded or published without an explicit
instruction.

## Runtime and trust

No hooks, no MCP server, no background process, no network fetch at load time.
The skills name commands an agent may run; the device-mutating and
outward-facing ones are listed in `SECURITY.md` and are treated as actions
needing a human's say-so. Documentation facts are quoted with the date they
were read, and each skill tells the agent to re-verify through
`metavr docs search` or the `llmstxt` address before relying on a number.

## Risk table

| Risk | Rating | Why |
|---|---|---|
| Executes code on install | Low | `bin/xr-dev.js` copies directories; refuses when the plugin is present |
| Reads credentials | None | nothing here reads or stores a secret |
| Network at runtime | None | the bodies point at URLs; nothing fetches on load |
| Mutates a device | Medium, gated | only through commands the agent runs deliberately (`metavr app install`, `files rm`, `shell`) |
| Outward-facing action | Medium, gated | `metavr store dist upload` is a draft unless `--publish`; the body says so |
| Stale content | Medium | platform docs move; every claim carries a read date and a re-verify instruction |

## Maintenance

Facts are re-checked against Meta's documentation each release; the VRC
reference is generated from Meta's page rather than transcribed. Issues about
an out-of-date claim are treated as bugs.
