# Browser runtime and delivery checks

**Read this when** planning a WebXR game, adding optional MR features, auditing compatibility or preparing browser/PWA delivery.

Use [Meta's WebXR/IWSDK documentation](https://developers.meta.com/horizon/documentation/web/), the [WebXR specification](https://www.w3.org/TR/webxr/) and the chosen framework's versioned examples. Checked 2026-09-21; support is negotiated with the actual browser/device.

## Define the browser contract

Record framework/browser versions, secure origin, supported session modes, input sources, required versus optional features, asset loaders/decoders and ordinary-screen behavior. A Quest native OpenXR extension or permission does not automatically exist in WebXR. Immersive VR and immersive AR support are separate checks.

Check session support before offering entry; start sessions through an appropriate user action and handle rejection. Request only required features as required; optional depth/anchors/hand tracking should not prevent the rest of the experience from running when unavailable. Do not infer browser support from headset model alone.

## Runtime acceptance

- Enter → interact → end → enter again; clean up session listeners/resources and stale references.
- Switch/disconnect input sources; validate grip versus target-ray spaces and button/hand alternatives.
- Handle visibility changes, tracking/reference-space changes and WebGL context loss without leaking assets or leaving a blank page.
- Maintain a useful mouse/touch/keyboard presentation when immersive mode is unavailable. Respect accessibility/reduced-motion behavior in the ordinary-screen surface.
- Bound frame allocations, network work, uploads and texture memory; profile representative mobile-browser rendering separately from desktop.

## Asset and deployment evidence

Validate exported scale, materials, compressed textures/meshes and animation against the actual loader extensions. Use LOD/instancing/culling deliberately; compare both visual quality and frame cost. Keep download size, GPU memory and decoder cost as separate measurements.

Test HTTPS, CORS, MIME types, cache invalidation and offline behavior chosen by the product. Configure cross-origin isolation only when the chosen runtime/threading path requires it, with its documented headers and third-party resource implications. Avoid serving stale HTML against new hashed asset manifests.

Browser hosting, installable PWA and a Store-listed wrapper are different delivery paths. Use current Meta PWA/Store guidance if that path is selected; do not apply native APK rules to an ordinary URL or assume a URL's availability equals Store approval. Record launch URL, build hash, tested browsers, modes and unavailable features.

## Evidence and fallback

Keep console/network traces, session errors, input checks and device frame measurements. A desktop emulation or static screenshot does not prove immersive interaction. If no WebXR device is attached, complete ordinary-screen and source/build tests and enumerate the remaining real-session checks.
