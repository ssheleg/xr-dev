# Packaging a WebXR site as a Quest PWA

**Read this when** a working WebXR page has to become an installable app —
`bubblewrap init` through to a sideloaded APK — or when an immersive PWA
refuses to launch.

Source: `documentation/web/pwa-packaging` (page dated 2026-07-22), read
2026-09-20 and verified against `@meta-quest/bubblewrap-cli` **1.24.1**.

## Contents

- Before the first command
- Initialise
- Signing
- Digital Asset Links — the step that decides whether it launches
- Build and sideload
- Failure modes

## Before the first command

- The site is served over **HTTPS** with a valid Web App Manifest.
- Node.js 18+, and `npm install --global @meta-quest/bubblewrap-cli` (Meta's
  fork, not Google's `bubblewrap`).
- An app exists in the Developer Dashboard; its **Meta Horizon Application ID**
  is needed if the PWA uses in-app purchases.
- IAP setup is done *before* packaging — billing is a `bubblewrap init` answer.

## Initialise

```bash
mkdir my-pwa && cd my-pwa
bubblewrap init --manifest=https://example.com/manifest.webmanifest --metaquest
```

Four answers matter:

| Prompt | Choose |
|---|---|
| App mode | `immersive` for a WebXR app that launches straight into a session; `2D` for a windowed site, **including screen-based 3D**. Stored as `horizonOSAppMode` in `twa-manifest.json` |
| Android package identifier | unique, and **identical for every future update** of a Store app |
| Display mode | `standalone` for 2D, with the orientation the panel actually uses |
| Horizon Billing | only with IAP; needs the Application ID |

## Signing

The Store requires a signed package. Let Bubblewrap create a key or point it at
an existing one — and for an update, **the same certificate as the previous
version**. Keep the keystore, alias and passwords somewhere that survives the
machine; a lost signing key ends the app's update path.

## Digital Asset Links — the step that decides whether it launches

A Trusted Web Activity verifies the package against the origin. **An immersive
PWA does not launch if this fails**; a 2D one falls back to custom-tab UI, which
looks like a styling bug rather than a verification failure.

```bash
keytool -list -v -keystore /path/to/android.keystore -alias android   # take SHA256
bubblewrap fingerprint add <sha256-fingerprint>                       # writes assetlinks.json
```

Publish it at `https://<origin>/.well-known/assetlinks.json` and confirm the URL
returns that JSON over HTTPS **before** testing the package. With more than one
trusted origin, host the file on each; the file is an array and can authorise
several packages on one origin, one statement per package and certificate.

`keytool` comes from the JDK Bubblewrap installed, if the shell has no other.

## Build and sideload

```bash
bubblewrap build          # prompts for the signing passwords
ls app-release-signed.apk
metavr app install app-release-signed.apk
```

## Failure modes

| Symptom | Cause |
|---|---|
| Immersive PWA never opens | asset-links verification failed — wrong fingerprint, file not published, or not served over HTTPS |
| 2D PWA shows browser chrome | same verification, softer failure |
| Store rejects the update | package identifier or signing certificate changed |
| Billing missing at runtime | Horizon Billing was not enabled at `init`; regenerate the project |
| Session starts only after a tap | the page waits for a gesture instead of requesting the session on load |
