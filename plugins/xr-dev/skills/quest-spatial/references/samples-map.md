# The 15 official samples, mapped to the question each answers

**Read this when** starting anything in Spatial SDK: the sample that already
does it is faster to read than the prose about it, and it compiles.

`github.com/meta-quest/Meta-Spatial-SDK-Samples` — MIT, 276 stars, read
2026-09-20. Each directory is a standalone Gradle project.

## Contents

- The map
- What a clone brings with it
- Running one

## The map

| I need to… | Sample |
|---|---|
| start from the smallest working app | `StarterSample` (the Getting Started / hello-world project) |
| move between a 2D panel app and an immersive one | `HybridSample` |
| define my own component shared across app instances | `CustomComponentsSample` (+ `CodelabStarters/CustomComponentsStarter`, the same app with the logic removed for the codelab) |
| play animation clips, drive animation from code | `AnimationsSample` |
| put 3D objects in a scene and tune them in Spatial Editor | `Object3DSample` |
| do the same with Interaction SDK grabbing | `Object3DSampleIsdk` |
| add physics and tune it in the editor | `PhysicsSample` |
| build an immersive video player | `MediaPlayerSample` (custom shaders — needs the NDK) |
| stream DRM-protected or 180° video, reflect panels into the room | `PremiumMediaSample` (needs no Spatial Editor) |
| play video with spatialised audio | `SpatialVideoSample` |
| react to the user's real room | `MixedRealitySample`, `MrukSample` (MRUK; needs no Spatial Editor) |
| read body-tracking skeleton joints | `BodyTrackingSample` |
| use the Horizon OS UI Set for consistent UI | `UISetSample` |
| render Gaussian splats | `SplatSample` |
| package reusable `SpatialFeature` library modules | `FeatureDevSample` |
| see complete apps rather than features | `Showcases/` |

## What a clone brings with it

The repository is **agent-configured**: `AGENTS.md` at the root and one per
sample, plus `.claude/`, `.cursor/`, `.opencode/`, `.roo/`, `.clinerules`,
`.windsurfrules`, `GEMINI.md` and `.aider.conf.yml`. Its root `AGENTS.md`
points at the same `llms.txt` index this pack uses.

**One trap in that convenience:** the repo's `.mcp.json` declares an MCP server
`hzdb` running `npx -y @meta-quest/hzdb mcp server` — the CLI's older name. On
a machine that already has `metavr` wired, opening a clone gives an agent **two
registrations of the same tool**, with the older package behind one of them.
Decide which one the session should use; do not run both (`quest-tooling` has
the rule).

## Running one

1. Clone, open the **specific sample directory** in Android Studio — not the
   repository root.
2. Plug in the headset (Developer Mode on), press Run.
3. Every sample except `MrukSample` and `PremiumMediaSample` needs **Meta
   Spatial Editor** installed.
4. `MediaPlayerSample` and `PremiumMediaSample` need the NDK, pinned in
   `app/build.gradle.kts` (`ndkVersion`).
5. The samples ship Meta's OVRMetrics integration — enable it to read frame
   numbers in the headset rather than guessing.
