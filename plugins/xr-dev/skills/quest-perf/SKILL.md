---
name: quest-perf
description: >-
  Use when a Meta Quest / Horizon OS app misses frames, judders, overheats or
  must be profiled — the frame budget per refresh rate, logcat stats, the GPU%
  number that lies during frame drops, Dynamic Resolution, foveation,
  Application SpaceWarp, and capturing with OVR Metrics, Perfetto, simpleperf or
  RenderDoc. Engine-independent. Triggers - "dropped frames" / "просадка кадров", "judder" /
  "джаддер", "Quest performance" / "производительность на Quest", "GPU bound" /
  "упёрлись в GPU", "profile the headset" / "профилировать шлем", "perfetto trace"
  / "трейс perfetto", "simpleperf", "RenderDoc", "OVR Metrics", "stale frames",
  "SpaceWarp", "foveated rendering" / "фовеальный рендеринг", "72 vs 90 Hz",
  "app is hot" / "шлем греется". NOT for wiring the render loop itself
  (quest-native), not for Store performance VRCs as a submission gate
  (quest-store), and not for desktop or mobile-phone profiling.
license: MIT
compatibility: Any agent can read this workflow. Live source checks need network; build, device, profiling and Store actions need the named installed tools and accounts. Missing capabilities use the inline fallback and leave dependent checks unverified.
metadata:
  version: "0.3.0"
---

# Quest performance: the budget, the lie, and the capture

Performance work on Horizon OS fails in one of two ways: optimising without a
capture, or reading the capture wrong. This skill fixes the second first, because
the most-quoted number on the platform — `GPU%` — is misleading exactly when it
matters.

For a whole-product roadmap or stage audit, use `quest-lifecycle`; a single technical task stays with this owner. If absent, identify the current stage, its evidence and the next prerequisite inline.

Read `references/mobile-rendering.md` when choosing the render pipeline or investigating tile, render-pass, geometry, overdraw and asset costs.

## The budget is a deadline, not a target

| Refresh rate | Time per frame |
|---|---|
| 72 Hz | 13.9 ms |
| 90 Hz | 11.1 ms |
| 120 Hz | 8.3 ms |

CPU, render-thread, GPU and compositor work form a pipeline and can overlap
across frames. Compare the critical path and synchronization against the
deadline; do not add independent CPU/GPU samples as a universal frame-time
formula. Missed submissions may invoke reprojection, with visible artifacts
that depend on motion, depth and the selected runtime path.

## The GPU% lie, and the 50% threshold

When an app drops to half rate the GPU finishes early and idles, so utilisation
*falls* while the app is firmly GPU-bound.

```text
FPS=36/72  Stale=36  GPU%=0.65  App=18.05ms
```

- `FPS=36/72` — half rate: every frame shown twice.
- `App=18.05ms` — the real per-frame GPU time, against a 13.9 ms budget.
- `GPU%=0.65` — measured across the doubled 27.8 ms interval, which is why it
  reads 65% while the app needs a **23% cut**, not the 35% "headroom" it implies.

**Rule: read `App` in milliseconds against the refresh-rate budget. Only trust
`GPU%` near saturation.** To climb back out of half rate, GPU work must fit one
refresh interval — i.e. utilisation must fall **below ~50%** while at half rate.

If `App` is inside budget and `Stale` remains non-zero, inspect CPU submission,
synchronization and compositor timing in a trace. That symptom alone does not
prove a CPU bottleneck. The worked half-rate example above assumes the stated
metric definitions and no intentional SpaceWarp mode; verify both first.

## Select a lever from the measured bottleneck

Read `references/rendering-playbook.md` when choosing multiview, render scale,
foveation, layers, assets, shaders or reprojection. It links each experiment to
its prerequisites, visual failure cases and target-device evidence.

1. **Dynamic Resolution** — tune render scale through the engine/SDK's supported
   control path; verify actual behavior rather than assuming the OS enables it.
2. **Foveation** — distinguish fixed from eye-tracked; test supported levels and
   quality. A simple shader can cost more with FFR than without it.
3. **Refresh rate** — request a rate the representative workload sustains; observe
   actual runtime and thermal behavior rather than promising an automatic rate change.
4. **Application SpaceWarp** — a supported depth/motion-vector integration with
   artifact and latency tests, not an automatic rescue or guaranteed percentage gain.

## Capture chain — what each tool answers

| Question | Tool | How |
|---|---|---|
| Am I missing frames at all, and where | logcat VrApi stats (`FPS`, `Stale`, `App`, `GPU%`) | `metavr log` / `adb logcat` |
| Live numbers inside the headset | OVR Metrics Tool (`ovrmetric` APK) | `metavr tools install ovrmetric`, then enable its overlay |
| CPU vs GPU, thread timeline, stalls | Perfetto | `metavr` MCP `start_perfetto_capture` → `stop_perfetto_capture` → `analyze_trace`, or the CLI equivalents |
| Which C/C++ functions burn the CPU | simpleperf | Android NDK's simpleperf against the running package |
| Which draw call, shader or render stage burns the GPU | RenderDoc Meta fork | `metavr tools install renderdoc`; draw-call trace, render-stage trace, Vulkan shader stats |

Meta ships task skills for two of these — `hz-perfetto-debug` and
`hz-simpleperf-debug`, plus `hz-vr-debug` for general on-device debugging. When
they are installed, this skill decides *what to measure* and they drive the tool.

`references/capture-playbook.md` holds the exact sequences, including what to
capture for a report that another agent can act on.

## Method, so a second capture means something

1. Reproduce on a **release build on a real headset**. A simulator run
   (`xrsim`, `spatialsim`) checks supported simulated behavior, not headset performance.
2. Note refresh rate and the resulting budget before looking at anything else.
3. Capture with the app in the *worst* scene, not the menu.
4. Change **one** thing; re-capture; compare `App` ms, not impressions.
5. Record the pair (before/after `App`, `Stale`, scene, build id) in the
   project's own notes — a performance claim with no capture is an opinion.

## Gotchas that cost a debugging round

- **A thermally throttled headset invalidates the comparison.** Long sessions
  drift; let it cool or state the temperature state with the number.
- **Dev-mode overlays and logging cost frames.** Measure with them off, then
  turn them on only to read the numbers you cannot get otherwise.
- **Counter semantics depend on capture/runtime mode.** Inspect timestamps and
  reprojection state before interpreting a stale-frame count as dropped work
  or pipeline latency.
- **Draw calls are a CPU cost and fill is a GPU cost.** Cutting draw calls on a
  fill-bound frame moves nothing, which is why the capture comes first.
- **WebXR has its own counters** — draw-call metrics in the browser docs; see
  `quest-webxr` before applying native advice to a web build.

*Frame budgets, the 65%/18.05 ms worked example and the recovery mechanisms were
read from `documentation/native/android/os-missed-frames.md` on 2026-09-20;
re-verify with `metavr docs search "missed frames"`.*
