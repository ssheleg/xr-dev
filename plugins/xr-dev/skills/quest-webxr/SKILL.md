---
name: quest-webxr
description: >-
  Use when the XR experience runs in the browser rather than as a native binary -
  WebXR in the Meta Quest Browser, IWSDK or three.js or A-Frame, packaging the
  site as a PWA with the Meta Quest Bubblewrap CLI, in-app purchases through
  Horizon Billing, remote debugging with Chrome DevTools, and getting a PWA onto
  the Store. Triggers - "WebXR", "immersive-vr session" / "иммерсивная сессия",
  "three.js on Quest" / "three.js на Quest", "A-Frame", "IWSDK", "PWA for Quest"
  / "PWA для Quest", "bubblewrap", "web app manifest for the headset",
  "browser on Quest" / "браузер в шлеме", "remote debug the headset browser" /
  "отладить браузер шлема", "web IAP" / "покупки в вебе". NOT for native OpenXR
  apps (quest-native), native profiling (quest-perf), or an APK submission
  (quest-store).
license: MIT
metadata:
  version: 0.1.3
---

# WebXR and PWAs on Horizon OS

The web path trades native performance for a deploy that is a `git push`. It is
the right choice for demos, catalogues, tools and anything that must also run
outside a headset — and the wrong one when the frame budget is already tight.

## The order that avoids rework

1. **Build the site and test it in the headset's Browser first.** A packaged PWA
   uses the *same rendering engine*, so every compatibility and performance
   problem is visible before packaging.
2. **Debug it remotely** — Chrome DevTools from the machine against the device,
   over the Android platform tools. The Browser specifications page carries the
   user-agent string and the supported content sizes.
3. **Package only when the page is right.**

## Entering immersive mode like a real app

A PWA launched from the headset's library should not show a 2D landing page. Ask
for the session as soon as the page has loaded:

```javascript
const supported = await navigator.xr?.isSessionSupported('immersive-vr');
if (supported) {
  const session = await navigator.xr.requestSession('immersive-vr');
  await renderer.xr.setSession(session);          // three.js
}
```

A-Frame does the same through `scene.enterVR()` on `renderstart`. Meta's own
snippets gate this on `window.getDigitalGoodsService !== undefined` — present
inside a packaged PWA, absent in the plain Browser — so the page still behaves
when someone opens the URL on a laptop.

## Which framework

| Choice | When |
|---|---|
| **IWSDK** (`npm create @iwsdk@latest`) | Meta's recommended path for both screen-based 3D and immersive WebXR; ships the testing story (IWER on desktop) and build/deploy guides |
| three.js | an existing three.js codebase, full control of the renderer |
| A-Frame | declarative scenes, fastest to a prototype |

Meta also ships the `hz-iwsdk-webxr` skill for the IWSDK path — use it for
IWSDK-specific work; this skill decides whether the web lane is the right one
and owns the packaging and distribution seam.

## Packaging as a PWA

Step by step, including the Digital Asset Links step that decides whether an
immersive PWA launches at all: `references/pwa-packaging.md`.

```bash
npm install --global @meta-quest/bubblewrap-cli    # verified at 1.24.1, Node 18+
bubblewrap --version
```

Prerequisites, in the order Bubblewrap will need them:

- the site served **over HTTPS** with a valid Web App Manifest;
- an app created in the Developer Dashboard — its **Meta Horizon Application
  ID** is required if the PWA uses in-app purchases;
- a signing key, or the details to create one during `init`;
- a headset in Developer Mode for sideload testing.

On first run Bubblewrap offers to download a matching JDK and Android
command-line tools; let it, unless the environment manages those itself. During
Quest initialisation it asks whether to include **Horizon Billing** — answer
with the Application ID ready if IAP is in scope, because adding it afterwards
means regenerating the project.

## Monetisation and platform features

In-app purchases in a WebXR PWA go through Horizon Billing plus the Digital
Goods API; achievements, leaderboards and add-ons have server-to-server APIs on
the web documentation index. Set IAP up **before** packaging.

## Distribution

A packaged PWA is an Android package and travels the same road as a native
build: release channels, review, VRC — see `quest-store`, and Meta's
`hz-store-pwa` skill for the PWA-specific store steps. 2D (non-immersive) PWAs
are judged against a subset of the VRCs, with a list of permissions that trigger
automatic rejection.

## Performance, honestly

- The browser has its own counters — draw-call metrics in the web docs — and the
  native profilers in `quest-perf` do not see inside the page.
- The frame budget is the same as native (13.9 ms at 72 Hz); the overhead is
  not. Measure in the headset, never in a desktop browser window.
- `requestAnimationFrame` on the `XRSession` is the frame clock; a page that
  keeps a DOM animation running alongside it pays twice.

## Where to read

```text
index:  https://developers.meta.com/horizon/llmstxt/documentation/web/llms.txt/
page:   https://developers.meta.com/horizon/llmstxt/documentation/web/<slug>.md
```

Useful slugs: `pwa-webxr`, `pwa-packaging`, `pwa-overview-gs`, `browser-specs`,
`browser-remote-debugging`, `3d-web`, `ps-iap`, `ts-webxr-perf-drawcall`.
IWSDK's own guides live under `documentation/iwsdk/guides/`.

## Gotchas

- **A 2D landing page inside a PWA reads as a broken app** — request the session
  on load.
- **`bubblewrap` is Meta's fork** (`@meta-quest/bubblewrap-cli`), not the Google
  package; the Quest-specific prompts only exist in it.
- **Billing is a packaging-time decision**, not a runtime one.
- **Testing in the desktop browser proves logic and lies about performance.**

*Read from the Meta web documentation (`pwa-webxr`, `pwa-packaging`, `3d-web`)
on 2026-09-20; versions there move — re-check `bubblewrap` and IWSDK versions
before quoting them.*
