# Platform coverage and research navigation

Date: 2026-09-21. Base: `7954ba2a884f5a71d7487981b4335c0ecdbc25d4`. The operator requested deeper Quest/Oculus VR/AR development, rendering and publishing coverage, plus an assessment of vLLM-Omni for the creative harness. This member change covers the platform skills; vLLM-Omni deployment research belongs to the family report and Foundry integration packet.

## Contract and scope

Retain the six existing skill owners, EN/RU trigger boundaries and distributable layout. Add task-triggered references inside their owning skill directories; keep bodies below their budgets. No new public release, installed-skill update, provider deployment or family submodule-pin change is part of this branch. Read `CLAUDE.md` and `docs/AGENT_SYNC.md`; guarded shared registry/release files are not edited.

| Requirement | Change | Verification |
|---|---|---|
| Q01 | Project target, engine/runtime lane, vertical slice, failure modes and evidence | Native playbook and adversarial scenario |
| Q02 | MR features, permissions, tracking/room lifecycle and camera/AI boundaries | MR reference; conflicting-camera and offline-AI scenarios |
| Q03 | Correct CPU/GPU reasoning and provide rendering decision experiments | Performance body/reference; overlap scenario |
| Q04 | Release manifest/source conflict handling, platform services and release evidence | Native/store references and Store scenarios |
| Q05 | Spatial build/audit fallback and measured budget interpretation | Spatial body/reference and existing panel scenario |
| Q06 | Gateway-aware tools, source navigation and absent-tool paths | Tooling body/reference and installation scenario |
| Q07 | Browser/session/assets/ordinary-screen delivery path | WebXR reference and browser capability scenario |
| Q08 | Portable distribution, source receipts and honest evaluation status | Existing gates, house audits, schema checks and handoff |

## Sources and findings before edits

- Existing `quest-perf` says combined CPU/GPU time must fit one refresh interval and infers CPU binding from stale frames alone. The requested fix is trace-based diagnosis with pipeline overlap and synchronization, not an unconditional sum.
- Existing `quest-spatial` turns isolated panel measurements into architectural ceilings. Reclassify these as workload-dependent planning estimates.
- Existing tooling examples configure an agent directly despite the operator's gateway policy. Preserve plugin-managed registration; standalone stdio uses the gateway on this estate, OAuth remains at the agent.
- Both the current Meta native and release manifest pages show `com.oculus.intent.category.VR`; this base teaches `IMMERSIVE_HMD` as the release requirement. Correct the cited requirement without deleting additional cross-runtime categories blindly.
- The updated Android-14 announcement explicitly narrows the requirement to apps created after March 1, 2026; the old forum announcement says all uploads. Prefer the amended primary announcement and retain the app creation date.
- Camera overview says either CAMERA or HEADSET_CAMERA; the native page says both. Do not resolve this by collecting permissions indiscriminately. Match the actual API/SDK, inspect the merged manifest and test with fresh permission/account state.

Primary documents checked: [native manifest](https://developers.meta.com/horizon/documentation/native/android/mobile-native-manifest/), [release manifest](https://developers.meta.com/horizon/resources/publish-mobile-manifest/), [Android 14 correction](https://developers.meta.com/horizon/blog/meta-quest-apps-android-14-march-1/), [camera overview](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-pca-overview/), [native camera](https://developers.meta.com/horizon/documentation/native/android/pca-native-documentation/), [FFR](https://developers.meta.com/horizon/essentials/fixed-foveated-rendering/), [compositor layers](https://developers.meta.com/horizon/essentials/compositor-layers/), [XR Operator](https://developers.meta.com/horizon/blog/meta-xr-operator-close-the-build-test-verify-loop-for-vr/). More sources are attached to their new reference modules. Local temporary source copies are not distributed.

## Evaluation and delivery

Preserve the existing behavior-result status: no independent model runs have been executed. Add adverse scenarios against the observed source failures before writing the changed procedures. Run package, negative, installer, strict plugin and eval-schema checks after the change. A structural pass does not prove headset performance, successful Store review or GPU inference.

Save a tracked handoff with exact files, checks, remaining behavioral/device work and remote branch. The family research index will link the pushed member commit. No second planning approval is required: this is the operator's authorized continuation and an isolated, reviewable skill change.
