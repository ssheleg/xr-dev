# Mixed reality capabilities and lifecycle

**Read this when** implementing passthrough, room understanding, anchors, hands/body/eyes, shared physical space, camera processing or AI input on Quest.

Sources checked 2026-09-21. Select a feature by the app's need and runtime support, not by “all SDK features.” The acceptance checks below are recommended project tests, not a claim that every row is a Store rule.

## Capability contract

For each feature record: API/SDK and source date; required versus optional; runtime support; manifest declaration; current permission grant; account/device restrictions; data lifetime; fallback; test scene and evidence. An available extension and a granted Android permission are separate facts. Inspect valid/tracked pose flags before using coordinates.

| Feature | Choose it for | Failure path to test |
|---|---|---|
| Displayed passthrough | Showing the real world behind/through virtual content | Unavailable session/mode, focus loss, transition back to VR; do not assume access to camera pixels |
| Scene/MRUK room model | Semantic surfaces, placement, generated room gameplay | Permission denied, no Space Setup, incomplete scan, changed room, rescan and unsupported semantics |
| Environment depth | Occlusion against the physical world | Unsupported/invalid depth; fall back visually, never treat it as authoritative collision/safety geometry |
| Spatial anchors | Stable real-world placement and later localization | Save/share/load failure, localization timeout, changed room, deleted anchor |
| Shared anchors/colocation | Aligning multiple users' coordinate systems | Anchor alignment success with network-state failure and vice versa; stale alignment and host loss |
| Hands/controllers | Interaction, gestures and haptics | Switching input source, tracking quality, occluded hands, controller disconnect, reserved system gesture |
| Body/face/eye data | Supported avatar/interaction requirements | Capability unavailable or consent refused; retain a usable avatar/input alternative |
| Raw passthrough camera | CV/ML, object recognition, QR/reference acquisition | Missing grant/device/account support, camera busy, invalid frame, changed resolution, resume after pause |

Primary maps: [passthrough](https://developers.meta.com/horizon/essentials/horizon-os-passthrough/), [spatial data permission](https://developers.meta.com/horizon/documentation/unity/unity-spatial-data-perm/), [MRUK features](https://developers.meta.com/horizon/documentation/unreal/unreal-mr-utility-kit-features/), [Shared Spatial Anchors sample](https://github.com/oculus-samples/Unity-SharedSpatialAnchors), [native feature samples](https://developers.meta.com/horizon/documentation/native/native-openxr-sdk-sample/).

## Camera facts that commonly get mixed together

Displayed passthrough, raw forward camera frames, environment depth, a saved scene mesh and MediaProjection/casting are distinct products. Their images, coordinate frames, permissions and availability are not interchangeable. An image that looks like the headset view may omit UI or cover a different field of view.

The [camera overview](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-pca-overview/) describes Quest 3/3S, Horizon OS v74+, Camera2-based access and either CAMERA or HEADSET_CAMERA. The [native camera page](https://developers.meta.com/horizon/documentation/native/android/pca-native-documentation/) also says both permissions are needed, while [MRUK's component](https://developers.meta.com/horizon/reference/mruk/v85/class_meta_x_r_passthrough_camera_access/) names HEADSET_CAMERA. Treat this as a documented discrepancy: use the chosen component's versioned requirements, inspect the merged manifest, request the minimum supported grant and verify a fresh install. Record unresolved conflicts; do not silently broaden permissions.

Query camera identity, supported output sizes and calibration metadata; never hardcode camera index, resolution or the assumption that it covers the user's full view. Keep capture timestamps and convert through the correct camera/head/world transforms before placing content. Close images, sessions, readers and GPU resources according to the API lifecycle; bound queues and drop stale frames rather than accumulating latency.

The overview states that the Passthrough Camera API is unsupported in XR Simulator. It also warns that parental restrictions may not be applied to an MQDH-installed app: developer sideloading cannot certify the release-channel age/account path. Validate that path separately. The [public-release announcement](https://developers.meta.com/horizon/blog/new-era-mixed-reality-passthrough-camera-api-machine-learning-computer-vision/) permits Store publication; do not repeat the obsolete blanket claim that camera apps cannot ship.

Camera data is Device User Data under the linked Meta policy. Explain capture/off-device use, minimize retention and redact diagnostics; apply the product's consent/privacy flow. Permission to render passthrough is not permission to upload room images to an AI service. Test denial/revocation without stranding the user.

## Shared physical play is more than anchors

Keep local tracking space, shared world transform and authoritative game simulation distinct. Share anchor identities/alignment under the chosen SDK; use an actual networking solution for object state, ownership, prediction/interpolation and reconnection. [Group Presence](https://developers.meta.com/horizon/documentation/native/ps-group-presence-overview/) reports destinations/joinability; it does not synchronize physics. Exercise invite/deep-link joining when the app is cold, active or already in another session.

Test two real accounts and devices in representative rooms, including non-joinable/private states. Bound avatar/network updates independently of the render loop. Include mute/block/report and data handling when the product has social/UGC features, under current platform policy.

## Comfort and interaction review

Consume the project's scenario set. Cover seated/standing reach, left/right-handed input, snap/smooth movement preferences, controller/hand alternatives, text angular size and distance, subtitles and non-audio feedback. World-lock stable content; use head-locked content deliberately. Do not force camera motion or hide tracking failure behind a seemingly stable world. Respect system focus/gestures and the OS boundary.

Use [Meta design guidance](https://developers.meta.com/horizon/design/) and a human headset review for comfort. Automated input, screenshots and static reach calculations cannot certify comfort or environmental safety.
