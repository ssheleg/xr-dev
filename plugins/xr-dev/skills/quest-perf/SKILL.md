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
metadata:
  version: 0.1.5
---

# Quest performance: the budget, the lie, and the capture

Performance work on Horizon OS fails in one of two ways: optimising without a
capture, or reading the capture wrong. This skill fixes the second first, because
the most-quoted number on the platform — `GPU%` — is misleading exactly when it
matters.

## The budget is a deadline, not a target

| Refresh rate | Time per frame |
|---|---|
| 72 Hz | 13.9 ms |
| 90 Hz | 11.1 ms |
| 120 Hz | 8.3 ms |

Combined CPU + GPU work must fit before the display refreshes. Miss it and the
compositor re-displays the previous frame with rotational reprojection
(TimeWarp): stable under head *rotation*, wrong under head *translation*, so the
user sees judder and black wedges at the periphery rather than a frozen image.

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

If `App` is inside budget and `Stale` is still non-zero, the bottleneck is on the
CPU side; go to simpleperf, not to shaders.

## The four levers, in the order they are worth pulling

1. **Dynamic Resolution** — the OS lowers render scale when frames drop and
   restores it later. Enable it early; on Quest 2 and later it is also the
   prerequisite for the highest GPU levels.
2. **Fixed Foveated Rendering** — cheap pixels at the periphery; with dynamic
   foveation the OS can raise the level under pressure.
3. **Refresh-rate honesty** — request 90 or 120 Hz only if the app sustains it.
   A steady 72 Hz beats a stuttering 90 Hz, and thermal pressure will throttle
   the rate back to 72 anyway, changing the budget under a running session.
4. **Application SpaceWarp** — opt-in, renders at half rate and synthesises the
   in-between frames from motion vectors plus depth. Up to ~70% more GPU
   headroom, paid for with motion-vector work and transparency limitations. It
   is an integration, never an automatic rescue.

## Capture chain — what each tool answers

| Question | Tool | How |
|---|---|---|
| Am I missing frames at all, and where | logcat VrApi stats (`FPS`, `Stale`, `App`, `GPU%`) | `metavr device logcat` / `adb logcat` |
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
   (`xrsim`, `spatialsim`) proves behaviour, never performance.
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
- **`Stale` equal to the refresh rate with steady FPS is pipeline latency**, not
  dropped work — a different problem with a different fix.
- **Draw calls are a CPU cost and fill is a GPU cost.** Cutting draw calls on a
  fill-bound frame moves nothing, which is why the capture comes first.
- **WebXR has its own counters** — draw-call metrics in the browser docs; see
  `quest-webxr` before applying native advice to a web build.

*Frame budgets, the 65%/18.05 ms worked example and the recovery mechanisms were
read from `documentation/native/android/os-missed-frames.md` on 2026-09-20;
re-verify with `metavr docs search "missed frames"`.*
