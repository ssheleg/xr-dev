---
name: quest-store
description: >-
  Use when getting a Meta Quest build to testers or into the Meta Horizon Store -
  the four release channels, what review actually checks (VRC technical then
  content), the release manifest that differs from the development one, Data Use
  Checkup, signing, uploading with metavr or the Oculus platform utility, store
  assets, and test accounts. Triggers - "publish to the store" / "выложить в
  стор", "Horizon Store", "App Lab", "release channel" / "релизный канал",
  "alpha build for testers" / "альфа для тестеров", "VRC", "app review" /
  "ревью приложения", "rejected by Meta" / "Meta отклонила", "Data Use Checkup" /
  "DUC", "upload apk to Quest store" / "загрузить apk в стор", "store assets" /
  "ассеты для стора", "test user" / "тестовый аккаунт". NOT for building the app
  (quest-native), profiling it (quest-perf), machine setup (quest-tooling), or a
  PWA listing (quest-webxr).
license: MIT
metadata:
  version: 0.1.4
---

# Shipping to the Meta Horizon Store

Two facts decide most of the schedule. **Every upload — alpha included — must
meet the full release packaging requirements.** And **the Production channel is
the only one that triggers review**; a build sitting there does nothing until
the submission info is filled in and "Submit for Review" is clicked.

## The four channels

| Channel | Audience | Review |
|---|---|---|
| ALPHA | invite-only, starts **empty — not even you** | none |
| BETA | invite-only | none |
| RC | invite-only | none |
| Production (Store) | everyone entitled | **technical + content review** |

- Invite by email, alias or URL, or mark a channel public so users subscribe
  themselves. Default limit **200 users per channel**, up to 2,500 on request.
- Testers see the build in their Library and under **My Preview Apps**.
- Copying an approved build into Production updates every entitled user.
- Distributing to testers in South Korea has its own GRAC rating requirement.

The useful consequence: a first playable can reach real testers with **no Meta
review at all** — as long as it is packaged like a release build.

## Review, in the order it happens

1. **Technical review** — the Virtual Reality Checks (VRC). A failure comes back
   as a detailed report naming each missed requirement; resubmission is normal.
2. **Content review** — completeness, polish and value, after the technical pass.
3. **Approval** — then a release date can be set, immediately or scheduled.

Plan **at least two weeks** before a target launch date. In saturated categories
review may stop at the first violation found, so self-checking is cheaper than
a round trip. Apps using platform features must file a **Data Use Checkup**
before submission; without a current DUC, platform features stay limited to
test users.

## What gets checked, grouped by what it costs to fix late

| Group | The ones that fail builds |
|---|---|
| Packaging | manifest conforms to the **release** spec (`.1`), **v2 signature** (`.2`), no unsupported Android features (`.3`), supported SDK/engine (`.4`), APK < 1 GB and OBB < 4 GB (`.5`), **64-bit only** (`.6`) |
| Performance | runs at the declared refresh rate (`.1`), head-tracked graphics or a VR loading indicator **within 4 s** (`.3`), ≥85% render scaling recommended (`.4`) |
| Functional | no crashes or freezes, pauses when the OS asks, never strands the user, no data loss, positional tracking honoured, works for **multiple entitled users**, passthrough loading screen when launched from MR Home |
| Input | **focus-aware** — keep rendering, hide hands, ignore input (`.4`); hand-tracking apps must respect the reserved system gesture |
| Security | minimum permissions and no unsupported ones (`.2`); an entitlement check within 10 s is a **recommendation**, not a requirement (`.1`) |
| Assets | logo on transparent background, no text in the top or bottom 20% of cover art, screenshots representative and free of other platforms' hardware, trailer **≤ 2 minutes**, text ≥ 24 pt |

The full tables, with which apply to immersive versus 2D apps, are in
`references/vrc-checklist.md`. Fetch the live list before a submission —
requirements retire and appear (`VRC.Quest.Performance.2` is RETIRED today).

## The release manifest is not the development manifest

Development requirements and submission requirements are two documents, and
only the second is enforced at review. Before uploading anything:

- `android:debuggable` false or absent — a release build, not a debug one.
- `installLocation="auto"`, unique `android:label`.
- Immersive: `android.hardware.vr.headtracking` `required="true"`; a 2D panel
  app omits it or sets `required="false"`.
- OpenXR apps: `org.khronos.openxr.intent.category.IMMERSIVE_HMD` alongside
  `LAUNCHER` in the intent filter.
- SDK levels: **an app created since 1 March 2026 must target 34**; recommended
  min 32 / target 34 / compile ≥ target for in-lifecycle devices.
- Sign with **APK signature scheme v2**; keep the keystore out of the repository.

`quest-native` carries the same contract from the build side.

## Uploading

```bash
metavr store dist apps                       # app ids in the organization
metavr store dist channels --app-id <ID>     # channels and their latest builds
metavr store dist upload --app-id <ID> --channel ALPHA --apk build.apk \
  --notes "what changed"                     # a DRAFT upload unless --publish
metavr store dist copy-build ...             # promote between channels
metavr store test-user ...                   # FRL test accounts for the org
```

`LIVE` is the store channel in that flag. The Oculus Platform Command Line
Utility (`metavr tools install platform-utils`) does the same job with
delta-patching for large packages, and MQDH is a GUI wrapper over it. Upload
validation reports packaging problems **after** the upload, so budget a
correction round.

**`versionCode` must increase with every build** or the upload is refused; the
version the testers see is `versionName`.

## A checklist that fits the two gates

Before the first ALPHA upload: release manifest, v2 signing, 64-bit, size
limits, `versionCode` bumped, it launches on a real headset from a cold boot.

Before Production: everything above plus the VRC self-pass, DUC filed if
platform features are used, store assets to spec, screenshots captured **in the
headset**, trailer under two minutes, age rating questionnaire complete, and the
privacy policy URL live.

## Gotchas that cost a submission round

- **"It is only an alpha" is not an exemption** from packaging requirements.
- **Channels start with nobody in them**, including the developer — an empty
  channel looks like a broken upload.
- **A Production build is invisible until submitted**; no review starts on
  upload alone.
- **2D panel apps are a different rule set**: a VRC subset, and a list of
  permissions (precise location, telephony, …) that trigger automatic rejection.
- **Store assets fail more submissions than code does.** Text bleeding into the
  unsafe top/bottom 20% is the classic.

*Channel behaviour, review stages, the VRC groups and the SDK-level rule were
read from developers.meta.com (`resources/publish-release-channels`,
`publish-app-review`, `publish-quest-req`, `publish-mobile-manifest`) on
2026-09-20. Re-check before a submission: these pages carry their own dates.*
