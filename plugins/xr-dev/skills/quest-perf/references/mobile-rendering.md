# Mobile rendering: experiments before prescriptions

**Read this when**: choosing an art/render pipeline or diagnosing costs that desktop intuition
misses. Sources checked 2026-09-21; no fixed scene-wide triangle/draw-call/texture
budget applies to every device, content type or renderer.

## Establish the workload

Record device/OS, graphics API, render pipeline, stereo mode, refresh target,
resolution, FFR/ETFR, MSAA, layers, lighting, animation/skinning, active cameras,
content and thermal state. Capture representative CPU/GPU/frame/memory baselines.
Use the same view and input sequence before/after; compare visual quality too.

## Tile-based GPU decisions

- Render-pass transitions and intermediate targets can cause costly stores,
  resolves and reads from shared memory. Inventory postprocessing, camera stacks,
  portals/reflections and copies before reducing asset quality indiscriminately.
- Test pass fusion/subpass or direct rendering where supported by the actual
  engine/backend. FFR/MSAA behavior depends on the target path; a screenshot of
  an enabled setting does not prove it applies to the final rendering.
- MSAA can be relatively efficient in tile memory, but higher sample counts still
  cost memory/bandwidth and interactions matter. Benchmark against the chosen
  resolution and shader workload rather than blanket-disable or max it.
- Expensive position/vertex work and triangles crossing many tiles affect binning.
  Inspect RenderDoc Meta Fork tile/render-stage evidence when available. Do not
  assume tile dimensions or quote an unverified per-triangle execution formula.
- Compare transparent/alpha-blended overdraw, particle layers and screen coverage;
  reduce what profiling implicates. Measure baked versus realtime lighting,
  shadows, shader variants and material complexity on the target.
- For assets, measure compressed and resident textures, mip use, mesh/skin/animation
  cost, LOD transitions, collisions, loading/upload stalls and memory peaks.
  Normal maps or impostors trade geometry for other costs; verify the trade.

## Advanced experiments and stop rules

Use the existing rendering playbook for multiview, foveation, dynamic resolution,
composition layers, symmetric projection, late latching and SpaceWarp. Every
proposal states prerequisite, expected bottleneck, quality risk, capture and
revert criterion. Do not enable multiple techniques then attribute a gain to one.
Low app GPU utilization alone is not spare frame budget; distinguish app render,
compositor, CPU scheduling and thermal behavior.

Keep spectator/capture cameras out of normal gameplay budgets unless shipped.
Profile representative sustained use and transitions, not just an empty scene.
A simulator can exercise logic/API availability; it cannot certify headset GPU,
comfort, thermal or Store performance. Never claim a fixed sum of CPU and GPU
intervals when stages overlap.

## Primary reading

- [Tile rendering](https://developers.meta.com/horizon/documentation/unity/gpu-tiled/): architecture and binning.
- [Improved algorithms](https://developers.meta.com/horizon/documentation/unity/gpu-improved-algorithms/): mobile-friendly tradeoffs.
- [Impaired algorithms](https://developers.meta.com/horizon/documentation/unity/gpu-impaired-algorithms/): pass/resolve and vertex costs; verify its unresolved formula separately.
- [Graphics pipeline](https://developers.meta.com/horizon/design/design-graphic-rendering-pipeline/): vocabulary, not a device feature support matrix.
- [Display](https://developers.meta.com/horizon/design/display/): stereo, color and capture presentation.
