# Spatial SDK build and audit procedure

**Read this when** implementing or auditing a Spatial SDK app, especially when Meta's `hz-spatial-sdk` companion or preferred MCP is absent.

Sources checked 2026-09-21: [development](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-development/), [samples](https://github.com/meta-quest/Meta-Spatial-SDK-Samples), [runtime guidelines](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-runtime-guidelines/), [camera overview](https://developers.meta.com/horizon/documentation/spatial-sdk/spatial-sdk-pca-overview/). Match the sample/SDK revision to the consumer; sample toolchain versions are not a mandate to upgrade every project.

## Inspect first

Read the Gradle wrapper, version catalog, AGP/Kotlin/JDK/SDK pins, application/activity classes, feature modules, ECS systems/components, scene assets and tests. Determine standalone immersive, panel or hybrid transitions; required interaction, media, physics, MRUK and camera features. Record the actual target OS/device and module support.

If no project exists, choose the smallest official sample matching the requirement and a compatible revision; carry only necessary modules/assets and their notices. Read project instructions in the sample as source context, not as authority to configure all agents or replace the family's pipeline.

## Implement one verified slice

1. Build the existing or selected sample with its wrapper before adding features. Inspect available Gradle tasks; run relevant compile/unit/lint/assemble tasks and retain output. A missing SDK/JDK receives a precise prerequisite diagnosis.
2. Register required features/components/systems and one scene. Make entity ownership/destruction, event subscriptions, coroutine cancellation and activity lifecycle explicit.
3. Add one panel and one interaction. Test focus, density/legibility, hit targets, layout updates and transition between 2D/immersive activities. Release surfaces/resources when their owner is destroyed.
4. Import one representative GLB/glXF asset with scale, materials, animations and collision checks. Use supported loaders/extensions; a generic glTF validator does not prove the SDK supports every extension.
5. Add permissions/capability checks before optional MR features. No room scan, refused camera access or invalid tracking must have a usable fallback. For shared platform behavior, use quest-native's MR reference through that skill.
6. Run a release build on the target device when available, exercise launch/resume/reopen and measure a representative mixed workload. Report device checks NOT-RUN when no headset is attached.

## ECS and panel audit

Check query scope and repeated entity lookups, structural churn/per-tick allocation, threading/ownership boundaries, stale component references, unbounded listeners and scene reload cleanup. Identify work that can be scheduled on events rather than every frame. Treat the measured EOPT/object/panel tables as estimates from their stated workload; combine real panels, assets, video and physics in a representative test.

Panels have Android lifecycle and input/audio behavior. Verify focus arbitration, media pause/resume, audio focus and accessibility; test a second immersive entry rather than only first launch. Known-issue workarounds must match the installed SDK before applying a downgrade or deprecated API.

## Advanced feature plan

For MRUK, anchors, camera/CV, custom shaders, media/DRM, animation, physics or shared sessions, name an official sample, supported API/version, failure case and verification scene. Validate only the modules required by the brief. Preserve platform capability checks separately from runtime permission grants and account restrictions.

Enumerate actual sample directories and build targets rather than trusting a README's prose count. Use the current SDK index to discover new modules; retrieve the relevant page and versioned API signature before implementation. A navigation skill should close a small task even when its accelerator is missing.

## Audit result

Return source-addressed findings with impact, reproduction and bounded fix; include target/dependency inventory, commands and unavailable checks. Build success, structural asset validity, visual correctness and headset performance are separate results. Hand performance to quest-perf and release evidence to quest-store.
