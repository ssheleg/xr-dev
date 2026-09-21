# Product and release evidence

**Read this when** planning publication, preparing a release candidate, integrating accounts/purchases/saves/social features or investigating a rejection.

Primary sources checked 2026-09-21. Re-fetch current requirements at submission and retain the app's dashboard context. Proposed evidence fields below are this pack's workflow, not extra Meta requirements.

## Distinguish distribution surfaces

Standalone Horizon OS APK, PC/Rift distribution, browser/PWA delivery and Horizon Worlds are different products. A mobile APK passing adb installation has not passed Store review. [App Lab content moved into Horizon Store](https://developers.meta.com/horizon/blog/get-apps-ready-app-lab-meta-horizon-store-meta-quest-developers/); do not present historical App Lab as today's separate uncurated channel.

Use [release channels](https://developers.meta.com/horizon/resources/publish-release-channels/) for invited testers. Record channel membership, entitlement, exact build and account/device coverage. SideQuest/sideloading is a separate delivery path and does not prove Store compliance. Enterprise/managed deployment needs its own current policy and device-management checks.

## Freeze the artifact being reviewed

Record commit and dependency locks, engine/SDK/build tools, package/app IDs, app creation date, versionName/versionCode, supported devices, APK hash, signing certificate identity and build variant. Keep the keystore and passwords outside Git and logs.

Inspect the **merged manifest in the built APK**, native library ABIs, package size and signature, not only source templates. Use installed Android SDK tooling such as `apkanalyzer` and `apksigner` after checking their local help. Save commands/results without secrets. Compare install, upgrade and cold launch from the actual release-channel build; debug, sideloaded and Link behavior are separate receipts.

## Resolve manifest and policy drift

The [release manifest](https://developers.meta.com/horizon/resources/publish-mobile-manifest/) currently shows `com.oculus.intent.category.VR` alongside MAIN/LAUNCHER for OpenXR apps, and `excludeFromRecents=true`. The [native development page](https://developers.meta.com/horizon/documentation/native/android/mobile-native-manifest/) also shows the Meta VR category. Do not treat a generic `IMMERSIVE_HMD` example as proof of this release contract; inspect the selected SDK's generated output and retain any additional required cross-runtime categories deliberately.

The [Android 14 announcement](https://developers.meta.com/horizon/blog/meta-quest-apps-android-14-march-1/) was amended on February 6, 2026: the target-34 requirement applies to apps created in the Dashboard after March 1, 2026, replacing the older all-uploads announcement. Record creation date and current upload validation instead of propagating the older forum wording. Android target/min/compile SDK and Horizon OS minimum-version gating answer different questions.

For other contradictions: record both URLs, update dates, exact app/API context and the observed validator/runtime behavior; prefer the current topic owner and relevant amended policy. If unresolved, report the requirement as unresolved instead of silently lowering it or collecting extra permissions. Review/approval status belongs to the actual dashboard, not a cached tutorial.

## Product-service checks

| Surface | What to verify before release | Primary entry |
|---|---|---|
| Entitlement and identity | Correct app/account; failure/offline behavior; no server secret in client; distinguish entitlement from purchase verification and attestation | [Platform introduction](https://developers.meta.com/horizon/documentation/unreal/ps-platform-intro/) |
| IAP/DLC/subscriptions | Correct SKUs/test users; cancellation, restore, already-owned/consumable behavior, server validation and idempotent grants | [Current app payment policy](https://developers.meta.com/horizon/policy/app-policies/) and Platform SDK docs |
| Saves and backup | Supported data location, exclusions, upgrade migration, uninstall/reinstall and restore; user opt-out | [Cloud Backup](https://developers.meta.com/horizon/documentation/unity/ps-cloud-backup/) |
| Multiplayer/social | Cold/warm deep link, invite, joinability, reconnect, account isolation, block/mute/report where applicable | [Group Presence](https://developers.meta.com/horizon/documentation/native/ps-group-presence-overview/) |
| Integrity | Threat model, backend token verification, expiry/replay handling and graceful failure | [Attestation API](https://developers.meta.com/horizon/documentation/native/ps-attestation-api/) |
| Camera/mic/AI/analytics | Actual data collected/transferred/retained, permission denial, account/age path, deletion/privacy and current Data Use Checkup | [Review guide](https://developers.meta.com/horizon/resources/publish-app-review/) and [camera overview](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-pca-overview/) |

Cloud Storage V2 was shut down on January 31, 2025 according to the Cloud Backup guide. Do not recommend it for a new app. Cloud Backup is filesystem backup/restore, not a multiplayer authority database or guaranteed immediate cross-device synchronization.

Payments depend on distribution and product type; apply the current policy and documented exceptions. Do not substitute an unrelated web-payment recipe for in-app digital purchases without checking those rules. Keep purchase authority and entitlement decisions on the appropriate trusted backend/SDK path.

## VRC and human review

Refresh the [VRC list](https://developers.meta.com/horizon/resources/publish-quest-req/) using the pack's generation process; do not edit a generated checklist as if its counts were permanent. Classify each applicable requirement with PASS/FAIL/NOT-RUN/N/A, exact build, reproduction and evidence. Mark recommendations as recommendations and retired entries as retired.

Cover startup/loading feedback, tracking/focus/background, crashes and memory pressure, input/system gestures, sustained frame rate, account changes, permissions and content-specific requirements. Include seated/standing/left-handed/accessibility and human comfort review through the project's scenario owner. Automated screenshots or XR Operator interactions cannot prove all these properties.

Store assets must represent the actual product/build. Verify current resolution/safe-area/text/trailer requirements, supported languages, content/age rating, privacy/support links and rights. Route shipped text/visuals through existing copy/design owners. Never invent certification or claim every screenshot is in-headset if only an editor capture exists.

## Release state and recovery

Track independently: built → signed/validated → uploaded → assigned to channel → tested → submitted → technical review → content review → approved → scheduled/released. A successful upload response proves one transition, not public availability. Confirm storefront/channel visibility with an eligible account.

Keep the previous known-good build and save-schema compatibility; document the currently supported rollback/promotion mechanism. If recovery requires a new upload, preserve signing identity and increase versionCode. Test backend compatibility across old/new clients before release. Capture rejection reasons against VRC IDs and resubmit the smallest verified correction.

After release, monitor crashes/ANRs, performance, purchase and restore failures, retention and user reports under approved data policy. Make monitoring ownership and rollback criteria explicit; a Store approval is not evidence that production remains healthy.
