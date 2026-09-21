# Rendering decisions and controlled experiments

**Read this when** choosing a render path, diagnosing an expensive scene, importing assets or integrating foveation, compositor layers, late latching or SpaceWarp.

Checked 2026-09-21. The tests below are engineering guidance. Use the engine/SDK's versioned documentation for switches; a native Vulkan extension name is not a Unity setting.

## Capture the right workload

Record build hash, engine/packages, graphics API, device/OS, refresh rate, render scale, CPU/render-thread/GPU times, waits, dropped frames, memory and sustained thermal state. Include scene/input, warmup and capture overhead. Compare the same workload before/after; average FPS hides spikes and half-rate operation.

CPU and GPU can process different frames concurrently. Diagnose the critical path and deadline, not a sum of independent durations. GPU idle time may be waiting for CPU submission; a CPU wait may be waiting for the GPU. Compositor scheduling, sync and asset uploads can also produce missed frames. [Unity profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html) documents these distinctions.

## Select an experiment from the evidence

| Suspected cost | Controlled change | Check for damage |
|---|---|---|
| CPU draw submission | Batching/instancing, culling, compatible multiview | Correct per-eye transforms/shaders, visibility, materials and animation |
| Pixel/fragment cost | Reduce render scale, shader complexity, transparent coverage or FFR | Text/edges, central/peripheral quality, scene readability |
| Bandwidth/tile stores | Reduce intermediate targets, resolves and full-screen passes; compatible subsampled layout | Alpha, MSAA/depth resolves, post effects and capture |
| Geometry/animation | LOD, skin/bone budgets, animation update policy | Silhouette, deformation, popping and physics consistency |
| Memory/residency | Mips/compression, bounded streaming, release unused assets | Unsupported importer extensions, texture color space, transition hitching |
| CPU simulation/GC | Fixed-step budget, pooled allocations, bounded AI/pathfinding/I/O | Gameplay determinism, collision and response latency |
| Load/warmup | Async loading, shader/pipeline warmup, progressive scene entry | First-use spikes and OS-compliant loading feedback |

Quest's mobile/tile GPU behavior differs from desktop preview. Prefer the engine's supported mobile renderer; desktop Lumen/Nanite/post-processing assumptions are not standalone evidence. Consult [Meta Vulkan/OpenGL guidance](https://developers.meta.com/horizon/documentation/unreal/os-vulkan-opengl/) and the exact engine compatibility matrix rather than applying one graphics API rule to every engine.

## Stereo, foveation and dynamic resolution

[Unreal Mobile Multi-View](https://developers.meta.com/horizon/documentation/unreal/unreal-multi-view/) reduces CPU stereo submission overhead and is a prerequisite there for SpaceWarp/late latching; it does not make pixel shading free. Check the equivalent Unity/native path, shaders and per-view resources.

[FFR](https://developers.meta.com/horizon/essentials/fixed-foveated-rendering/) is fixed-center and distinct from eye-tracked foveation. It helps appropriate fill-heavy workloads but can cost more than it saves for simple shaders. Test quality levels and compatible subsampled layout on each supported target. Query ETFR support rather than inferring it from a model name. Text that must remain sharp may belong on compositor layers.

Dynamic resolution changes render scale, not the simulation budget. Verify the selected engine/SDK's control path and interaction with manual scale, FFR and frame-rate policy. Record hysteresis/quality limits and sustained behavior. A feature being available does not mean it is already enabled by the OS.

[Symmetric projection](https://developers.meta.com/horizon/documentation/native/android/os-symmetric-projection/) changes eye frusta/render areas and can combine with supported Vulkan foveation/optimization paths. Preserve correct view/projection math and test clipping/per-eye edges. Evaluate it after a working baseline; do not hand-modify matrices merely because a tutorial reports a gain.

## Layers, alpha and color

[Compositor layers](https://developers.meta.com/horizon/essentials/compositor-layers/) can improve text/UI/video clarity, but have a rendering, memory and per-layer cost. Choose overlay versus underlay deliberately; verify alpha semantics, depth/occlusion and transparent ordering. Do not keep unused zero-alpha layers alive as a free placeholder. Confirm linear/sRGB conversions, supported swapchain formats and the selected engine's premultiplication convention; compare a color/alpha test pattern in the headset.

For exported assets inspect post-import triangles/vertices, material slots/draw submissions, texture residency, mips, decoder support and bounds. A smaller compressed file may decode slowly or require an unavailable extension. Preserve masters, measure the scene after import and use the project's target profile instead of a universal polygon limit.

## Reprojection and latency

TimeWarp, application SpaceWarp and application rendering are different stages. [Application SpaceWarp](https://developers.meta.com/horizon/documentation/unreal/unreal-asw/) requires a supported engine/runtime integration, including depth/motion data. Test thin geometry, disocclusion, transparency, particles, UI and controller motion. No advertised percentage is a guaranteed budget increase for this scene.

Late latching/prediction affects pose-to-display latency; it cannot repair an incorrect simulation, invalid pose or blocking network call. Verify engine support and input path. Retain full-rate rendering as a measured comparison when evaluating half-rate synthesis.

## Deliver evidence, not a list of toggles

For each optimization retain settings diff, trace/capture, metric distributions, visual regressions and an explanation of the bottleneck addressed. Report a sustained device result or NOT-RUN; simulator/remote PC rendering is not a headset thermal test. Change one variable per experiment unless a documented dependency requires a group.
