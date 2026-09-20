# Session, frames and focus

**Read this when** wiring or reviewing the OpenXR lifecycle of a native app:
instance and session creation, the event loop, frame pacing, swapchains, and
the focus rules review enforces.

Source: Meta's OpenXR core-concept pages under
`documentation/native/android/mobile-openxr-*` plus the OpenXR 1.0 specification
(khronos.org), read 2026-09-20. **Names and structs are checked against the
spec before use — this file is the shape of the loop, not an API reference.**

## Contents

- Startup order
- The event loop and session states
- The frame loop
- Swapchains
- Focus, pause and the VRCs they map to

## Startup order

1. `xrGetInstanceProcAddress(XR_NULL_HANDLE, "xrInitializeLoaderKHR", …)` —
   the loader function is fetched with a **null instance**.
2. `xrInitializeLoaderKHR` with `XrLoaderInitInfoAndroidKHR`
   (`applicationVM`, `applicationContext`) — extension
   `XR_KHR_loader_init_android`.
3. Enumerate extensions; decide what the app can use from what came back.
4. `xrCreateInstance` carrying `XrInstanceCreateInfoAndroidKHR`
   (`XR_KHR_android_create_instance`).
5. `xrGetSystem` for a head-mounted display, then graphics-binding requirements
   (`XR_KHR_vulkan_enable2` or the GLES equivalent) — **query the requirements
   before creating the device**, they constrain instance and device extensions.
6. `xrCreateSession`, then reference spaces (`STAGE` for room-scale, `LOCAL` for
   seated; recentre behaviour differs and `VRC.Quest.Functional.9` requires a
   forward-orientation reset in `LOCAL`).

## The event loop and session states

`xrPollEvent` every frame, drained to empty. The state machine — not a boolean —
decides the lifecycle:

| Event state | Action |
|---|---|
| `IDLE` | wait; no frames |
| `READY` | `xrBeginSession` |
| `SYNCHRONIZED` | frames are submitted, but nothing is visible |
| `VISIBLE` | rendering is seen; input is **not** yours |
| `FOCUSED` | the only state where the app owns input |
| `STOPPING` | `xrEndSession` |
| `LOSS_PENDING` / `EXITING` | tear down, recreate or quit |

Treat `VISIBLE` and `FOCUSED` as different worlds: the system menu leaves an app
visible and unfocused, and that is the case most apps get wrong.

## The frame loop

```text
xrWaitFrame   -> predictedDisplayTime, shouldRender
xrBeginFrame
  xrLocateViews(predictedDisplayTime)      // pose EVERYTHING at this time
  render each view into its swapchain image
xrEndFrame(predictedDisplayTime, layers)
```

- Rendering to "now" instead of `predictedDisplayTime` produces judder that no
  profiler explains, because the frame was on time and simply wrong.
- `shouldRender == false` still requires `xrEndFrame` — with no layers.
- Submit the layers the frame actually has; a stale layer is displayed again.
- Frame budget by refresh rate and what happens when it is missed: `quest-perf`.

## Swapchains

- `xrEnumerateSwapchainFormats` and pick from the result. A hardcoded format is
  a portability bug that surfaces on the next headset.
- Acquire → wait → render → release, per image, per view. The wait has a
  timeout; ignoring its result is how a frame renders into an image the
  compositor is still reading.
- Colour space is declared (`XR_FB_color_space`), never assumed; the default
  differs from what a desktop renderer expects.

## Focus, pause and the VRCs they map to

| Behaviour | VRC |
|---|---|
| Keep rendering while unfocused, hide hands and controllers, ignore input | `VRC.Quest.Input.4` |
| Pause single-player gameplay when the OS asks | `VRC.Quest.Functional.2` |
| Head-tracked graphics or a VR loading indicator within 4 s of launch | `VRC.Quest.Performance.3` |
| Never strand the user with no way forward | `VRC.Quest.Functional.3` |
| Respect the reserved system gesture in hand tracking | `VRC.Quest.Input.8` |

These are review gates, so they belong in the loop from the first commit rather
than in a pre-submission sprint.
