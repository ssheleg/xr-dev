# Navigating 197 Spatial SDK pages

**Read this when** a Spatial SDK question needs the authoritative page and
guessing the slug would waste a round trip.

Index (plain Markdown, no login):
`https://developers.meta.com/horizon/llmstxt/documentation/spatial-sdk/llms.txt/`
Any page: same path with `<slug>.md`. Counted 2026-09-20: 197 pages.

## Contents

- Core model
- Panels
- Interaction, UI and input
- Scene, assets and rendering
- The room, tracking and media
- Tooling and debugging
- Spatial Editor
- Platform services, billing and the Store
- Performance and limits

## Core model

| Question | Slug |
|---|---|
| What is the architecture | `spatial-sdk-architecture`, `spatial-sdk-explainer` |
| The ECS data model | `spatial-sdk-ecs`, `spatial-sdk-component`, `spatial-sdk-builtin-components`, `spatial-sdk-systems`, `spatial-sdk-writing-new-system` |
| Querying the data model | `spatial-sdk-queries`, `spatial-sdk-changedsince-query`, `spatial-sdk-childrenof-query`, `spatial-sdk-filters`, `spatial-sdk-attributes` |
| Activity lifecycle and the scene | `spatial-sdk-activity-lifecycle`, `spatial-sdk-scene`, `spatial-sdk-understand-scenes` |
| Reusable feature modules | `spatial-sdk-spatialfeature` |
| Events | `spatial-sdk-events` |

## Panels

`spatial-sdk-2dpanel` and its seven siblings: `-registration`, `-spawn`,
`-communication`, `-compose` (Jetpack Compose inside a panel), `-resolution`,
`-layers` (layer versus mesh rendering), `-drm`. Plus `spatial-sdk-panel-tutorial`
and `spatial-sdk-resize-panel`.

## Interaction, UI and input

`spatial-sdk-isdk-overview` and four more (`-grabbable`, `-panels`,
`-listen-to-input-events`, `-supporting-systems`); `spatial-sdk-inputs-controllers`;
the Horizon OS UI Set as ten component pages (`spatial-sdk-ui-button`, `-card`,
`-control`, `-dialog`, `-dropdown`, `-input`, …).

## Scene, assets and rendering

`spatial-sdk-3dobjects`, `spatial-sdk-gltfs`, `spatial-sdk-glxf` (the scene
composition format), `spatial-sdk-animations`, `spatial-sdk-physics`,
`spatial-sdk-custom-shaders`, `spatial-sdk-custom-components`,
`spatial-sdk-blend-modes`, `spatial-sdk-sorting`, `spatial-sdk-environment`,
`spatial-sdk-splats` (Gaussian splats), `spatial-sdk-passthrough`.

## The room, tracking and media

`spatial-sdk-mruk` and `spatial-sdk-mruk-hifi-scene` (Mixed Reality Utility
Kit), `spatial-sdk-scanner-overview` + `-api`, `-llama`, `-ot` (object
tracking), `spatial-sdk-pca-overview` + `-kotlin-api` (passthrough camera
access), `spatial-sdk-media-playback`, `spatial-sdk-audio`,
`spatial-sdk-spatial-audio`.

## Tooling and debugging

`spatial-sdk-development`, `spatial-sdk-hot-reload`, `spatial-sdk-android-studio-plugin`,
`spatial-sdk-validate-xml`, `spatial-sdk-tooling-dmi`,
`spatial-sdk-tooling-castinputforward`, `spatial-sdk-ovrmetrics`,
`spatial-sdk-known-issues`, plus 24 `ts-*` pages shared with the rest of the
platform (`ts-adb`, logcat, profilers, device setup).

## Spatial Editor

20 `spatial-editor-*` pages: `-download-setup`, `-overview`, `-components`,
`-compositions`, `-asset-library`, `-assetlib`, `-create-app-content` (the
codelab), `-command-line-interface`, `-ai-scene-manipulation`, `-bug-report`.

## Platform services, billing and the Store

43 `ps-*` pages — `ps-get-started`, `ps-entitlement-check`, `ps-iap` (+ `-s2s`,
`-test`), `ps-leaderboards`, `ps-achievements`, `ps-challenges`,
`ps-cloud-backup`, `ps-attestation-api`, `ps-deep-linking`, `ps-language-packs`,
`ps-presence`, `ps-ownership`. Google-Play-billing compatibility has three of
its own: `horizon-billing-compatibility-sdk`,
`horizon-billing-implement-google-play-billing-interface`,
`horizon-billing-known-limitations`. Submission itself is `quest-store`.

## Performance and limits

`spatial-sdk-runtime-guidelines` (the budgets), `spatial-sdk-design-tips`,
`os-compositor`, `os-compositor-layers`, `os-cpu-gpu-levels`, `po-memory-ram`,
`platform-audio`. Reading a capture is `quest-perf`.
