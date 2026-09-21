---
name: quest-native
description: >-
  Use when building or reviewing a NATIVE Meta Quest / Horizon OS app in C or C++
  against OpenXR — the Android manifest and Gradle contract, the Khronos OpenXR
  loader, session and frame loop, swapchains, Vulkan, passthrough, scene, hand
  tracking, and the SDK levels the Store now demands.
  Triggers - "OpenXR app" / "приложение на OpenXR", "native Quest app" / "нативное
  приложение для Quest", "Quest C++" / "Quest на плюсах", "AndroidManifest for VR" /
  "манифест для VR", "openxr_loader_for_android", "xrCreateInstance",
  "xrWaitFrame", "targetSdk for Quest" / "какой targetSdk для Quest",
  "IMMERSIVE_HMD", "hello_xr", "passthrough in native" / "passthrough нативно".
  NOT for Unity or Unreal engine implementation, not for
  a Kotlin Spatial SDK app, not for WebXR or a PWA (quest-webxr), not for
  profiling (quest-perf), not for Store submission (quest-store).
license: MIT
compatibility: Any agent can read this workflow. Live source checks need network; build, device, profiling and Store actions need the named installed tools and accounts. Missing capabilities use the inline fallback and leave dependent checks unverified.
metadata:
  version: "0.3.1"
---

# Native OpenXR on Horizon OS

A Quest app written in C or C++ talks to the headset through **OpenXR** and to the
phone-class OS underneath through **Android**. Most of what breaks sits in that
seam: a manifest that is legal for sideloading and illegal for the Store, a loader
version that crashes instead of degrading, a frame loop that stops drawing the
moment focus is lost.

Read `references/project-playbook.md` for project discovery, target/version
contracts, engine handoff, a vertical slice and an audit. Read
`references/mixed-reality.md` for feature/permission decisions, tracking/room
lifecycle, colocation and camera or AI input.

For a whole-product roadmap or stage audit, use `quest-lifecycle`; a single technical task stays with this owner. If absent, identify the current stage, its evidence and the next prerequisite inline.

## Step 0 — is this project even on this lane?

| The project is | Owner |
|---|---|
| C / C++ against OpenXR, Gradle + NDK | **this skill** |
| Unity | Meta's `hz-unity-*` skills (12 of them: core SDK, MRUK, movement/retargeting, quest-ui, passthrough camera, placement, platform SDK, project analyzer, TMP, FBX import, face tracking, code review) |
| Unreal | `https://developers.meta.com/horizon/llmstxt/documentation/unreal/llms.txt/` |
| Kotlin / Spatial SDK | Meta's `hz-spatial-sdk` |
| WebXR, IWSDK, PWA | `quest-webxr` in this pack |
| An existing 2D Android app | Meta's `hz-android-2d-porting` |

Being on the wrong lane costs more than any single bug in this file: Unity answers
do not transfer to a NativeActivity, and OpenXR extension names do not transfer to
Unity's OVR wrappers.

## Step 1 — verify, then answer

Horizon OS ships on its own cadence and the API surface moves with it. Any claim
about a Quest API, a required SDK level or a manifest element is checked against
Meta's own docs **before** it reaches code:

```bash
metavr docs search "openxr swapchain"          # the CLI; the MCP server exposes the same search
```

Every documentation page has a Markdown twin — no HTML scraping, no login:

```text
index:  https://developers.meta.com/horizon/llmstxt/documentation/native/llms.txt/
page:   https://developers.meta.com/horizon/llmstxt/documentation/native/android/<slug>.md
```

`references/doc-map.md` holds the slugs worth knowing by heart. If Meta's
`hz-quest-verify-first` skill is installed it enforces this check on its own —
read its result rather than repeating the search.

## Step 2 — the manifest, which is two manifests

**Development and release requirements differ, and only the release set is
enforced at review** (`VRC.Quest.Packaging.1`, `.4`). Writing the dev manifest and
submitting it without checking the release delta can fail review.

Current Meta manifest segment for an immersive OpenXR app (rechecked 2026-09-21):

```xml
<uses-feature android:name="android.hardware.vr.headtracking"
              android:required="true" android:version="1" />
<!-- in the launching activity -->
<intent-filter>
  <action   android:name="android.intent.action.MAIN" />
  <category android:name="android.intent.category.LAUNCHER" />
  <category android:name="com.oculus.intent.category.VR" />
</intent-filter>
```

- `android.hardware.vr.headtracking` with `required="true"` is what makes the app
  an immersive app; a 2D panel app omits it or sets `required="false"`.
- `android:screenOrientation="landscape"`, theme
  `Theme.Black.NoTitleBar.Fullscreen`, and the long `configChanges` list from the
  manifest doc. **Never `noHistory`.**
- Release only: `android:debuggable` false or absent, `installLocation="auto"`,
  a unique `android:label`, and `com.oculus.supportedDevices` listing
  `quest2|questpro|quest3|quest3s` — a device outside that list runs in
  compatibility mode and reports itself as an older generation.
- A pure NativeActivity app may ship `android:hasCode="false"`. The Platform SDK
  is a Java library: adding it removes that option.

Full element-by-element contract, both manifests side by side:
`references/manifest-and-gradle.md`.

## Step 3 — SDK levels, which changed in 2026

Recommended for in-lifecycle devices (Quest 2, Pro, 3 family): **minSdk 32,
targetSdk 34, compileSdk ≥ targetSdk**. The legal range is minSdk 29–34 and
targetSdk 32–34 for immersive apps (32–36 for 2D panel apps) — but **an app
created since 1 March 2026 must target 34**. Read the two tables from the source
before pinning them; they are quoted with their date in
`references/manifest-and-gradle.md`.

**A lock file is not the build.** Grep `build.gradle` AND whatever dependency
lock the project keeps: on 2026-09-20 in `elements-vr` the gradle said
`targetSdk 34` and `dependencies.lock.json` still said `32`, which is a release
note written against a build that does not exist.

## Step 4 — the loader, and the two extensions before any of your code

```gradle
android { buildFeatures { prefab true } }
dependencies { implementation 'org.khronos.openxr:openxr_loader_for_android:<ver>' }
```

- Meta supports the **Khronos** Android loader; no proprietary loader exists any
  more. **Below 1.0.34 the app crashes** — it does not fall back.
- Apps on the Khronos loader crash on Horizon OS older than **v62**, and a
  non-Quest-1 user below v62 never sees the update in the Store.
- `XR_KHR_loader_init_android`: fetch `xrInitializeLoaderKHR` through
  `xrGetInstanceProcAddress` with a **null instance**, call it with
  `XrLoaderInitInfoAndroidKHR`, and only then create anything.
- `XR_KHR_android_create_instance`: the Android-specific parameters ride into
  `xrCreateInstance` through it.

## Step 5 — the frame loop that passes review

- Drive the session off `xrPollEvent`; the state machine, not a boolean, decides
  when to begin and end the session.
- `xrWaitFrame` → `xrBeginFrame` → render → `xrEndFrame`, and pose everything at
  the **predicted display time** the wait returned. Rendering to "now" is judder
  with a clean profile.
- **Focus-aware is a VRC, not a nicety** (`VRC.Quest.Input.4`): when the app
  loses focus it keeps rendering, hides its hands and controllers, and ignores
  input. An app that freezes on the system menu fails review.
- Enumerate swapchain formats with `xrEnumerateSwapchainFormats` and pick from
  what came back; a hardcoded format is a portability bug waiting for the next
  headset. Colour space is explicit (`XR_FB_color_space`), not assumed.
- 64-bit binaries only (`VRC.Quest.Packaging.6`); APK under 1 GB, OBB under 4 GB
  (`.5`).

Session states, pacing and the focus rules in detail: `references/frame-loop.md`.

## Step 6 — capabilities, never device models

Check the feature through the chosen SDK/runtime, not just "is this a Quest
Pro". OpenXR extension enumeration is one layer; system properties, permissions,
account restrictions and valid tracking state may also be required. Camera2
capabilities do not reduce to OpenXR extension names. Compatibility mode can
change the reported model, so device-name checks alone are insufficient.

## What this skill hands off

| Next question | Where |
|---|---|
| It runs but drops frames | `quest-perf` (frame budget, the GPU% trap, capture tooling) |
| How do I get it onto a headset / read its logs | `quest-tooling` (metavr CLI + MCP, adb, simulator) |
| How do I ship it | `quest-store` (channels, VRC, DUC, upload) |
| A WebXR or PWA build instead | `quest-webxr` |

## Gotchas that cost a debugging round

- **The dev manifest passes sideloading and fails review.** Two documents, two
  requirement sets; the release one is `resources/publish-mobile-manifest`.
- **A wrong launch category** can look like a rendering bug. The current Meta
  release page names `com.oculus.intent.category.VR`; verify the merged APK
  against that page and the selected SDK rather than a generic OpenXR snippet.
- **Loader below 1.0.34 crashes on launch** with no diagnostic pointing at the
  loader.
- **`hasCode="false"` and the Platform SDK are mutually exclusive** — an
  entitlement check (`VRC.Quest.Security.1`, a recommendation rather than a
  requirement) pulls Java into a native app.
- **Samples are the fastest correct answer.** `hello_xr` (Khronos) and Meta's
  OpenXR SDK samples — `XrPassthrough`, `XrSceneModel`, `XrHandsAndControllers`,
  `XrSpaceWarp`, `XrSpatialAnchor`, `XrVirtualKeyboard` — each demonstrate one
  extension end to end. Read the sample before writing the extension by hand.

*Documentation facts above were read from developers.meta.com on 2026-09-20;
re-verify with `metavr docs search` before quoting a number back to anyone.*
