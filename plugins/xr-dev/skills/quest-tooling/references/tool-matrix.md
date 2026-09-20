# The managed developer tools, and what each is for

**Read this when** deciding what to install on a machine, or when a workflow
names a tool that is not there yet.

`metavr tools list` is the live answer on any machine; the table below says what
each one is *for*, and which need a headset. Sizes and versions measured on
macOS arm64 on 2026-09-20.

## Contents

- The matrix
- What to install for which job
- Measured install notes

## The matrix

| Tool | Size | Needs a headset | For |
|---|---|---|---|
| `perfetto` | — | for capture | Trace analysis; the UI and trace processor behind `metavr perf` |
| `renderdoc` | 257 MB | yes | Meta's RenderDoc fork: draw-call, render-stage and shader-stat captures |
| `ovrmetric` | 175 KB | yes (APK) | OVRMonitorMetricsService — live FPS / stale / GPU overlay in the headset |
| `meta-perf-service` | — | yes | On-device performance streaming plus a host CLI |
| `platform-utils` | 117 MB | no | Oculus Platform Command Line Utility — build uploads with delta patching |
| `xrsim` | 324 MB | no | Meta XR Simulator: run a spatial app on the machine |
| `spatialsim` | 651 MB | no | Android emulator for spatial computing (`metavr ssim`) |
| `xroperator` | 17 MB | a running XR app | MCP proxy letting an agent inspect and drive a live XR application; federates into metavr's MCP server |
| `haptics-studio` | 268 MB | for preview | Design and preview controller haptics |
| `spatial-editor` | 219 MB | no | 3D scene editor for spatial experiences |
| `unity-hub` | — | no | Unity Editor management — only for the Unity lane |
| `jdk` | — | no | Eclipse Temurin JDK 17, when the machine has no usable Java |

## What to install for which job

| Job | Install |
|---|---|
| Native or Unity app, profiling it | `perfetto`, `renderdoc`, `ovrmetric` |
| Shipping to the Store | `platform-utils` |
| No headset on the desk | `xrsim`, `spatialsim` |
| An agent that should see inside a running app | `xroperator` (then `metavr xroperator status`) |
| Controller haptics design | `haptics-studio` |
| Unity project | `unity-hub` (Meta's `hz-unity-*` skills own that lane) |

## Measured install notes (2026-09-20, macOS arm64)

- `perfetto`, `renderdoc`, `platform-utils`, `xroperator`, `xrsim`,
  `spatialsim`, `ovrmetric` installed cleanly and appear in `tools list`.
- `haptics-studio` installs into `/Applications` and **still reports `No`** in
  `metavr tools list` — the listing detects some tools by a path it does not
  use for a `.app` bundle. Check `/Applications` before reinstalling.
- `meta-perf-service` failed with *"this tool's release feed has no
  `<enclosure>` yet (no published build)"* — nothing is wrong locally; there is
  no build on this platform/channel yet.
- `metavr tools install` takes one tool at a time and needs no `-y`.
