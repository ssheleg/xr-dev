# Project discovery, implementation and audit

**Read this when** starting a Quest project, entering an unfamiliar repository, planning a vertical slice or deciding which engine/platform procedure to use.

Checked 2026-09-21. Procedures below are this pack's engineering contract; linked platform behavior comes from the named primary sources. A source audit is useful without an engine, MCP or headset; label unavailable checks NOT-RUN.

## Establish the target before choosing libraries

Record in the consuming project's existing architecture/evidence location:

| Field | Inspect or decide |
|---|---|
| Deliverable | Standalone Horizon OS APK, PC OpenXR executable over Link, browser WebXR, Android panel/hybrid, or a separate Horizon Worlds experience |
| Source | Commit, dirty changes, project files, build scripts, asset import configuration and dependency locks |
| Engine | Native/Spatial/Unity/Unreal/Godot version, renderer, plugin/SDK versions and matching build/export tools |
| Runtime | Device and Horizon OS, OpenXR runtime/loader, refresh rate, supported capabilities, permissions and account state |
| Product | VR/MR mode, seated/standing/roomscale, input options, offline behavior, save/account/network needs |
| Delivery | Package ID, signing owner, app ID/creation date, channel, supported devices and asset target profile |

Do not use “Oculus” alone as a build target. Legacy Rift/PC or Go tutorials, standalone Quest and Meta's current Android surface have different rendering, lifecycle and distribution paths. Link testing is not a standalone APK test. Android API level is not a Horizon OS feature version.

## Engine handoff

| Evidence | Procedure and primary entry |
|---|---|
| CMake/NDK/NativeActivity/OpenXR | This skill; [Meta samples](https://github.com/meta-quest/Meta-OpenXR-SDK) and [Khronos SDK source](https://github.com/KhronosGroup/OpenXR-SDK-Source) |
| Kotlin + `com.meta.spatial` | `quest-spatial`; [Spatial samples](https://github.com/meta-quest/Meta-Spatial-SDK-Samples) |
| Unity ProjectSettings/Packages/Assets | Discover available `hz-unity-*` skills; otherwise [Unity getting started](https://developers.meta.com/horizon/documentation/unity/unity-tutorial-hello-vr/), locked packages, scene/prefab inspection, EditMode/PlayMode and Android build |
| Unreal `.uproject`/Plugins/Source | [Meta compatibility matrix](https://developers.meta.com/horizon/documentation/unreal/unreal-compatibility-matrix/); choose Epic+plugin versus Meta fork deliberately; inspect assets/Blueprint/C++, cook/package and device render path |
| Godot `project.godot`/scenes/resources | [Godot XR setup](https://docs.godotengine.org/en/stable/tutorials/xr/setting_up_xr.html) and [Android export](https://docs.godotengine.org/en/stable/tutorials/xr/deploying_to_android.html); match engine/templates/vendor extension and renderer |
| Browser application | `quest-webxr`; native OpenXR extensions are not browser APIs |

Use engine companions if installed; never invent their tools. This platform skill supplies requirements and evidence, not Unity APIs inside a C++ project. For Godot, the setup/deployment pages currently disagree on Mobile versus Compatibility recommendations for Quest. Pin a release and test the required renderer/extensions on target hardware before choosing. Native engine compilation is needed only for an actual engine modification or custom template requirement.

## Build a representative vertical slice

1. Preserve the existing project. Reproduce its current build before scaffolding missing pieces.
2. Implement launch → tracked view/input → one real interaction → save/resume → exit. Add one MR capability only if it is required by the brief.
3. Import one representative source asset; check scale, axes, pivot, collision, material extensions, texture formats, skin weights and animation. Keep the editable master and import settings.
4. Keep gameplay simulation separate from rendering and asynchronous I/O. Budget physics, AI, navigation, animation, audio and asset loading as well as draw work. Avoid per-frame allocations and unbounded event subscriptions.
5. Exercise focus loss, permission refusal, tracking loss, input-source changes, background/resume and a second entitled account where applicable. Reset global/static state between sessions.
6. Produce the actual target build, install/cold-start it and capture representative sustained behavior. A successful editor, simulator or headless import check proves only that surface.

## Audit output

For each finding record severity, source location, observed/expected behavior, reproduction, affected targets, bounded fix and verification. Separate measured defect, source-risk, documented upstream limitation and NOT-RUN. Do not award a whole-project score from file names or a single screenshot.

Suggested evidence files, only if the project has no equivalent: `docs/xr/target.md`, `docs/xr/capabilities.json`, `docs/xr/verification.md`. Do not create a competing registry when the project's existing plan/scenario/evidence owners already hold these facts.

## Runtime AI is a separate latency and data path

Generation servers such as [vLLM-Omni](https://github.com/vllm-project/vllm-omni) can supply prepared speech/images/video or asynchronous NPC services. They do not provide collision-ready geometry or a replacement for the OpenXR frame loop. Route production assets through the configured asset/job owner, such as Asset Foundry when present; use delivered manifests and target gates.

Keep requests asynchronous, bound the queue and payload, cancel/ignore obsolete results using scene/session IDs, and cache approved fallbacks. Continue tracking/rendering and essential interactions when offline. Benchmark network/queue/inference/audio-playout separately from frame time; no universal latency claim follows from “streaming.” For camera/microphone input, apply the MR permission/data contract before any off-device transfer.

For small on-device CV, evaluate [Meta's Unity Inference Engine sample](https://developers.meta.com/horizon/documentation/unity/unity-pca-sentis/) against the exact model/operators and headset GPU budget. A model loading successfully does not prove it coexists with 90 Hz rendering.
