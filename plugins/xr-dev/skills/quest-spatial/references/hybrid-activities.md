# Hybrid panel and immersive activities

**Read this when**: one app must move between 2D panels and immersion or keep both active.
Primary source: [hybrid apps](https://developers.meta.com/horizon/documentation/spatial-sdk/hybrid-apps-overview/),
read 2026-09-21. Use its activity/intent details with the actual SDK; its example
OS target is not a mandate to downgrade or freeze a current application.

1. Model entry from Home, launch over another app, return to Home and reopening
   after process death. Decide **exclusive** (one active experience) versus
   **cooperative** (panel and immersive visible/interactable together).
2. Exclusive transitions may finish the prior activity after the next starts.
   Do not apply that pattern to a cooperative overlay: it destroys the panel
   the user asked to keep. Scope each cleanup to the transition that owns it.
3. Inspect the final manifest and activity graph. The source distinguishes
   `com.oculus.intent.category.2D` / `.VR`, a standard Android launcher fallback,
   `VR_HOME_LAUNCHER` and `OVERLAY_LAUNCHER`. Verify OS/SDK support and exact
   intent/PendingIntent contract in current docs before implementing.
4. Own persistent domain state outside Activity lifetime. Save serializable
   content/selection/work progress, not surfaces or XR handles. Use explicit
   cross-activity state/intent contracts, reject stale messages and prevent
   concurrent writes. Reconstruct runtime resources on resume.
5. Budget active panels and immersive work together. Suspend only work no longer
   visible/needed; assign camera/audio/input ownership deliberately. Distinguish
   Android activity lifecycle from OpenXR session/focus lifecycle.
6. Test Home/default launch, cooperative overlay, exclusive return, repeated
   transitions, back/menu, headset sleep, tracking/permission loss, activity
   recreation, process kill and task restoration. Check unsaved-work recovery,
   no duplicate sessions/audio, focus routing and no stranded blank view.

No headset: implement state-transition tests and inspect merged manifest, but mark
OS presentation, compositor/input behavior and combined performance NOT_RUN.
