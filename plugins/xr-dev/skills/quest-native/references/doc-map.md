# Where the answer lives: Meta's documentation as addresses

**Read this when** a question needs the authoritative answer and the search
would otherwise be a guess — or when an agent has no MCP server and must fetch
pages directly.

Verified 2026-09-20: every documentation page has a Markdown twin that returns
`200` with no login and no HTML furniture.

## Contents

- URL patterns
- Index pages, per build path
- Native slugs worth knowing
- Through the CLI instead

## URL patterns

```text
docs index:    https://developers.meta.com/horizon/llmstxt/documentation/<platform>/llms.txt/
docs page:     https://developers.meta.com/horizon/llmstxt/documentation/<platform>/<slug>.md
resources:     https://developers.meta.com/horizon/llmstxt/resources/<slug>.md
design/policy: https://developers.meta.com/horizon/llmstxt/{design,policy}/llms.txt/
API reference: https://developers.meta.com/horizon/reference/<sdk>/<version>/index.md
```

`<platform>` is one of `native`, `unity`, `unreal`, `spatial-sdk`,
`android-apps`, `web`. `<sdk>` takes `latest` where it exists (Spatial SDK
pins a version instead).

## Index pages

| Build path | Index |
|---|---|
| Native | `documentation/native/llms.txt/` (~395 links) |
| Unity | `documentation/unity/llms.txt/` |
| Unreal | `documentation/unreal/llms.txt/` |
| Spatial SDK | `documentation/spatial-sdk/llms.txt/` |
| Web / WebXR | `documentation/web/llms.txt/` |
| Android apps (2D) | `documentation/android-apps/llms.txt/` |
| Design | `design/llms.txt/` |
| Policy | `policy/llms.txt/` |
| Resources (publishing) | `resources/llms.txt/` |

## Native slugs worth knowing

All under `documentation/native/android/` unless noted.

| Topic | Slug |
|---|---|
| OpenXR support, loader, samples | `mobile-openxr` |
| Manifest (development) | `mobile-native-manifest` |
| Manifest (release) | `resources/publish-mobile-manifest` |
| Environment setup | `book-native` |
| Device setup, developer mode | `mobile-device-setup` |
| ADB on Quest | `ts-adb` |
| Frames and synchronisation | `mobile-openxr-frames` |
| Swapchains | `mobile-openxr-swapchains` |
| Actions and bindings | `mobile-openxr-actions-actionsets-bindings` |
| Missed frames, budgets, GPU% | `os-missed-frames` |
| Logcat stats definitions | `ts-logcat-stats` |
| OVR Metrics Tool | `ts-ovrmetricstool` |
| Perfetto traces | `ts-perfettoguide` |
| Simpleperf | `ts-simpleperf` |
| RenderDoc (Meta fork) | `ts-renderdoc-for-oculus`, `ts-renderdoc-capture`, `ts-renderdoc-drawcall`, `ts-renderdoc-renderstage`, `ts-renderdoc-shaderstats` |
| Vulkan validation layers | `ts-vulkanvalidation` |
| Vulkan vs GLES | `os-vulkan-opengl` |
| Application SpaceWarp | `os-app-spacewarp`, `mobile-asw` |
| Fixed Foveated Rendering | `os-fixed-foveated-rendering` |
| Dynamic Resolution | `dynamic-resolution` |
| Display refresh rate | `mobile-display-refresh-rate` |
| Passthrough | `mobile-passthrough`, `mobile-passthrough-bp`, `mobile-passthrough-loading-screens` |
| Scene and anchors | `openxr-scene-overview`, `mobile-scene-api-ref`, `openxr-ssa-share-content` |
| Hand tracking | `mobile-hand-tracking`, `native-multimodal`, `mobile-openxr-hand-tracking-microgestures` |
| Body / eye / face tracking | `move-body-tracking`, `move-eye-tracking`, `move-face-tracking` |
| Minimum OS versions | `documentation/native/min-os-versions` |
| Compatibility mode | `os-compatibility-mode` |

Publishing slugs live in `quest-store`'s own reference.

## Through the CLI instead

```bash
metavr docs search "passthrough loading screen"
metavr docs fetch  documentation/native/android/mobile-passthrough.md
metavr docs api-search "xrCreateSession"
```

The MCP server exposes the same three as tools, which is the path an agent
should prefer: it tracks the CLI version and needs no URL.
