---
name: quest-spatial
description: >-
  Use when a Meta Quest app is built with Meta Spatial SDK — Kotlin and Android
  rather than Unity or raw OpenXR: whether that lane is right, the toolchain it
  demands, the ECS model, panels as real Android views, hybrid apps, the runtime
  budgets that decide a design, the known issues that waste a day, and which
  sample or documentation page answers a given question. Triggers - "Spatial SDK" /
  "Спатиал SDK", "Meta Spatial SDK", "Kotlin app for Quest" / "приложение на
  Kotlin для Quest", "spatial panels" / "панели в VR", "Spatial Editor",
  "hybrid app" / "гибридное приложение", "glXF", "MRUK", "com.meta.spatial",
  "how many panels can I open" / "сколько панелей выдержит", "Spatial SDK
  samples" / "примеры Spatial SDK". NOT for native C++ OpenXR (quest-native),
  Unity (Meta's hz-unity-* skills), WebXR (quest-webxr), profiling a build
  (quest-perf), or Store submission (quest-store).
license: MIT
compatibility: Any agent can read this workflow. Live source checks need network; build, device, profiling and Store actions need the named installed tools and accounts. Missing capabilities use the inline fallback and leave dependent checks unverified.
metadata:
  version: "0.3.1"
---

# Meta Spatial SDK: the Android lane onto Horizon OS

Spatial SDK lets an **Android** team ship an immersive app in Kotlin: Android
Studio, Gradle, Jetpack Compose, the libraries they already use — with OpenXR
underneath and an ECS data model on top. A panel in the scene is a real Android
view, not a texture someone drew to look like one.

For a whole-product roadmap or stage audit, use `quest-lifecycle`; a single technical task stays with this owner. If absent, identify the current stage, its evidence and the next prerequisite inline.

Read `references/hybrid-activities.md` when mixing panel and immersive activities: exclusive/cooperative modes, state ownership and transition tests.

## Step 0 — is this the right lane?

| The team and the app | Lane |
|---|---|
| Android developers; panels, 2D UI, media, an app that is *also* a 2D app | **Spatial SDK** — this skill |
| Maximum control of the renderer, custom Vulkan, a game engine of your own | `quest-native` (C/C++ OpenXR) |
| Existing Unity content, a Unity team, asset-store pipeline | Meta's `hz-unity-*` skills |
| Ships on the web, or must run outside a headset too | `quest-webxr` |
| An existing 2D Android app that only needs to run on Quest | Meta's `hz-android-2d-porting` — porting, not rebuilding |

Spatial SDK is built around panels and an ECS scene. Use the runtime estimates
below to choose a representative workload early, not as hard API ceilings.
Read `references/build-and-audit.md` when implementing or auditing a project;
it provides the inline procedure when Meta's companion is absent.

## Step 1 — inspect the actual toolchain

Sample snapshot read on 2026-09-20 (`meta-quest/Meta-Spatial-SDK-Samples`, MIT).
Read the consumer wrapper/catalog first; do not upgrade an existing project
to these values without checking its SDK and build compatibility:

| Piece | Version |
|---|---|
| Headset | Quest 2 / 3 / 3S / Pro on Horizon OS **v69 or newer** |
| Android Studio | **Narwhal (2025.1.1) or newer** — required by AGP 8.11 |
| Gradle | **9.4.1** (wrapper) |
| Android Gradle Plugin | **8.11.1** |
| Kotlin | **2.1.0** |
| JDK | **17** (bundled with Android Studio; separate only for command-line builds) |
| Meta Spatial Editor | required by every sample **except** `MrukSample` and `PremiumMediaSample` |
| NDK | only for custom shaders (`MediaPlayerSample`, `PremiumMediaSample`) |

**The upgrade trap, stated by Meta:** AGP 8.5 or earlier running the Gradle 9.x
wrapper fails during native/CMake model sync, because that AGP calls a Gradle
API removed in Gradle 9. Moving AGP to 8.11.1 resolves it — the error message
does not point there.

Dependencies are modular; take what the app uses:
`com.meta.spatial:meta-spatial-sdk` (core, always), `-vr` (immersive
functionality, most apps), `-toolkit` (the common components and systems),
`-physics`, `-ovrmetrics`, and the rest listed in
`documentation/spatial-sdk/spatial-sdk-packages`.

## Step 2 — the budgets, before the architecture

Meta publishes workload estimates and recommendations
(`spatial-sdk-runtime-guidelines`, rechecked 2026-09-21). Use them in the first
sketch, retaining their device/content/refresh assumptions:

| Measured/recommended item | Snapshot estimate |
|---|---|
| Entity operations per tick (a read or write in a system) | **2,000** |
| Physics objects | **500** |
| 3D GLB objects in view | **100** when they cover >50% of the viewport; more only if they cover less |
| Scene-graph entities | **~1,000** |
| Panel resolution cost | each extra **480,000 pixels ≈ +1% GPU** |

The panel tables describe isolated test workloads and differ by *kind*:

| Panel type | FPS dips below 90 | FPS stays below 90 |
|---|---|---|
| Empty view | 20 | 40 |
| UI-only view | 15 | 40 |
| Image view | 15 | 40 |
| Web view | 5 | 30 |
| **Video view** | **3** | 5 |
| **Activity-based** | **2** | 2 |
| Panel with layers | 5 | 15 |

These measurements do not establish a hard three-video/two-activity limit or
guarantee that mixed workloads fit. Test the real panel/media/object mix in a
release build; consider reuse/virtualization instead of scaling panels with items.

## Step 3 — the traps that cost a day each

Full text and workarounds: `references/budgets-and-traps.md`.

- **Debug builds are much slower than release** — Meta lists it as a known
  issue, not as a surprise. Judge performance on the **release** variant, or
  the numbers mean nothing.
- **Entering immersive can kill other apps' audio.** Request
  `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK` unless exclusive audio is genuinely
  required, and handle `OnAudioFocusChangeListener`.
- **`finish()` on an immersive activity may not bring the 2D panel back**, and
  with panels on `enableLayer = true` it can crash inside
  `libMetaSpatialSDK.so`. `enableLayer` is deprecated — use `layerConfig`.
- **`PanelRenderMode.Mesh()` still creates a compositor layer**; the workaround
  is `panelConfig.layerConfig = null` after converting the settings.
- **Layers sharing one `SceneSwapchain` ignore per-layer `setClip()`** — all
  show the last clip set.

## Step 4 — where to read

The index is `documentation/spatial-sdk/llms.txt/`, and every page has a
Markdown twin at `documentation/spatial-sdk/<slug>.md`. The prefix says which
question a page answers. Counts below are the dated source snapshot, not a live inventory:

| Prefix | Count | Holds |
|---|---|---|
| `spatial-sdk-*` | 97 | the SDK itself: `-ecs`, `-component`, `-systems`, `-queries`, `-2dpanel-*` (8), `-isdk-*` (5, interaction), `-ui-*` (10, the Horizon OS UI Set), `-mruk`, `-physics`, `-animations`, `-glxf`, `-gltfs`, `-custom-shaders`, `-hot-reload`, `-known-issues`, `-runtime-guidelines` |
| `spatial-editor-*` | 20 | the visual editor, its CLI, asset library, compositions |
| `ps-*` | 43 | platform services: entitlement, IAP, leaderboards, achievements, cloud backup, attestation |
| `ts-*` | 24 | troubleshooting: adb, logcat, profilers, device setup |
| `os-*`, `po-*`, `platform-*` | 5 | compositor, CPU/GPU levels, memory, audio |
| `hybrid-*`, `horizon-billing-*`, `add-spatial-sdk-to-app` | 5 | hybrid apps and Google-Play-billing compatibility |

Slug tables worth keeping open: `references/docs-map.md`.

## Step 5 — the samples answer faster than the prose

`github.com/meta-quest/Meta-Spatial-SDK-Samples` (MIT). Enumerate its current
sample directories rather than relying on a prose count. Open the one
that already does what is being built — `references/samples-map.md` maps each
sample to the question it answers, and notes that the repository ships its own
`AGENTS.md`, `.mcp.json` and per-agent configuration, so an agent can be
pointed straight at a clone.

## Hybrid apps, in one paragraph

A hybrid app moves between 2D panel activities and immersive activities in one
package. Panel activities run in three contexts — **Home**, **Overlay** (the
Quest-button menu) and **Embedded** inside an immersive activity. Two
interaction models: **exclusive** (one at a time; terminate the old activity
*after* starting the new one) and **cooperative** (several concurrent).
`HybridSample` is the reference implementation.

## What this skill hands off

| Next question | Where |
|---|---|
| Write the ECS code, panels, gradle wiring | Meta's `hz-spatial-sdk` when present; otherwise this skill's build/audit procedure |
| It runs but drops frames | `quest-perf` |
| Get it onto a headset, read logs, capture | `quest-tooling` |
| Ship it | `quest-store` |

*Versions, budgets and known issues above were read from the samples repository
and `developers.meta.com` on 2026-09-20; both move — re-check with
`metavr docs search "spatial sdk runtime guidelines"` before quoting a number.*
