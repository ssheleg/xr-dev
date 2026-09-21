# Choose and research the actual build path

**Read this when**: engine selection or an inherited repository. Verify versions before a
setup change; source entry points checked 2026-09-21. The platform menu is a set
of choices, not a list of components every project installs.

| Evidence / intended surface | Start here | Spike and boundary |
|---|---|---|
| Unity Assets/Packages/ProjectSettings | [Meta Unity index](https://developers.meta.com/horizon/llmstxt/documentation/unity/llms.txt/); package lock; installed hz-unity-* catalog | Android/OpenXR + chosen render pipeline, input and MR vertical slice on lowest device; match Unity/Meta package compatibility, do not force latest |
| Unreal .uproject/Plugins/Config | [Meta Unreal index](https://developers.meta.com/horizon/llmstxt/documentation/unreal/llms.txt/); engine and Meta plugin releases | Android packaging and mobile rendering first; desktop Lumen/Nanite settings are not a standalone Quest performance plan |
| project.godot/.tscn/.gd | [Godot XR](https://docs.godotengine.org/en/stable/tutorials/xr/index.html); [Android export](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html); [Godot OpenXR Vendors](https://github.com/GodotVR/godot_openxr_vendors) | Match engine/export templates/vendor plugin and renderer; prove OpenXR action map, reference space, Android build and target feature; never treat GodotPrompter as engine authority |
| CMake/C++/Gradle | quest-native; [native index](https://developers.meta.com/horizon/llmstxt/documentation/native/llms.txt/) | Loader, extensions, graphics binding, swapchain/frame/session lifecycle and final manifest |
| Kotlin Spatial activities/entities | quest-spatial; [Spatial index](https://developers.meta.com/horizon/llmstxt/documentation/spatial-sdk/llms.txt/) | Match SDK/Gradle/JDK and samples; ECS/assets/panels; hybrid transitions if needed |
| Existing Android 2D app | [Android index](https://developers.meta.com/horizon/llmstxt/documentation/android-apps/llms.txt/); hz-android-2d-porting if present | Resizable panel, lifecycle/input/permissions and platform-service substitutions; check dependencies on unavailable mobile services |
| HTML/JS immersive browser session | quest-webxr; [web index](https://developers.meta.com/horizon/llmstxt/documentation/web/llms.txt/) | HTTPS, optional WebXR support, session/input/frame lifecycle, performance and useful non-XR route |
| Packaged immersive PWA | quest-webxr + quest-store | Browser runtime plus Android packaging, verified origin/asset links and applicable Store checks |
| Link PC VR or Horizon Worlds | Correct PC/Worlds documentation and target-specific product owner | Do not reuse Android APK, mobile GPU or Quest Store requirements as universal rules |

## Research contract

Read the platform index, then the exact API version used in the repository,
release notes, official sample and open issues relevant to the observed failure.
Record device/OS, engine/SDK/plugin versions and graphics backend in every bug or
performance prompt. Fetch only selected pages; a full index is navigation, not
material to inject repeatedly into the agent context.

Use [Meta's companion catalog](https://github.com/meta-quest/agentic-tools) when
available. The pinned 2026-09-21 inspection of commit
`18b183dfcb6a5fcec6615d882ca6922c08b7094f` found Unity-specific specialists,
Spatial, Android, WebXR, platform, design and Store workflows. It did **not**
justify promising a named Unreal implementation specialist. Use the Unreal docs
and engine workflow inline if no relevant specialist resolves.

For tools, inspect host capabilities rather than equating Claude Code with every
agent. MCP/plugins, portable skills and a CLI are separate installation surfaces.
A generic 3D asset search result still needs rights, scale, topology, UV, material,
texture/memory, collider, LOD and engine-import checks. Optional remote generation
must remain outside the critical frame loop, with budget/cancellation/offline paths.
