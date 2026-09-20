# Budgets, and the issues Meta lists against itself

**Read this when** sizing a Spatial SDK design, or when something behaves
strangely and the cause might already be documented.

Sources, read 2026-09-20: `spatial-sdk-runtime-guidelines` (page dated
2025-10-06) and `spatial-sdk-known-issues` (dated 2026-04-02). Both move —
re-fetch before quoting a number onward.

## Contents

- CPU budgets
- GPU budgets
- Memory
- Known issues and their workarounds

## CPU budgets

| Item | Max at 90 FPS |
|---|---|
| EOPT — entity operations per tick (a read or write to the data model inside a system) | 2,000 |
| Physics objects (a simple GLB with Physics) | 500 — graphics usually binds first |

Panels, by kind. "Dips" is the count at which spawning one more drops the frame
rate temporarily; "stays" is where it no longer recovers:

| Panel type | FPS dips below 90 | FPS stays below 90 |
|---|---|---|
| Empty view | 20 | 40 |
| UI-only view | 15 | 40 |
| Image view | 15 | 40 |
| Web view | 5 | 30 |
| Video view | 3 | 5 |
| Activity-based | 2 | 2 |
| Panel with layers | 5 | 15 |

An app may spend its CPU on any linear combination of objects and panels — the
two tables trade against each other rather than adding up independently.

## GPU budgets

- Up to **100 GLB objects in view** when they cover more than 50% of the
  viewport; fewer objects if they fill more of it.
- Panel resolution scales roughly linearly while fill-bound: a default panel at
  about half the screen is ~1000×750, and **every additional 480,000 pixels
  costs about 1% of the GPU**. Production apps have reached ~25 million pixels
  by that arithmetic.

## Memory

About **1,000 entities in the scene graph**, provided the CPU and GPU limits
above are respected.

## Known issues and their workarounds

| Issue | What happens | Workaround |
|---|---|---|
| **Debug-build performance** | debug variants run markedly slower than release | profile and judge UX on the **release** variant (Build Variants → release) |
| **Audio focus** | entering immersive stops or de-spatialises other apps' audio; it may not resume | request `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK` unless exclusive audio is required; implement `AudioManager.OnAudioFocusChangeListener`; test with music playing |
| **2D panel does not return** | `finish()` on an immersive activity can leave the panel activity gone; with `enableLayer = true` panels it can crash (`SIGSEGV`) in `libMetaSpatialSDK.so` | `enableLayer` is deprecated — configure `layerConfig: LayerConfig?`; follow the page's transition sequence rather than calling `finish()` blind |
| **Mesh render mode still makes a layer** | `PanelRenderMode.Mesh()` creates a compositor layer as well, costing GPU memory | after `panelSettings.toPanelConfigOptions()`, set `panelConfig.layerConfig = null` |
| **Shared swapchain clipping** | several `SceneQuadLayer`s on one `SceneSwapchain` all show the last `setClip()` region | Meta suggests pinning SDK 0.7.2 where this matters; otherwise give each layer its own swapchain |

## The toolchain failure that reads as something else

AGP **8.5 or earlier** with the **Gradle 9.x** wrapper fails during native/CMake
model sync — that AGP calls a Gradle API removed in Gradle 9. The message
blames CMake. Upgrade AGP to 8.11.1 (Android Studio's AGP Upgrade Assistant
does most of it).
