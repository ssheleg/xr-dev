# The manifest and Gradle contract, both halves

**Read this when** writing or reviewing an `AndroidManifest.xml` or `build.gradle`
for a native Quest app, or when a build is rejected for `VRC.Quest.Packaging.1`
or `.4`.

Sources: [native manifest](https://developers.meta.com/horizon/documentation/native/android/mobile-native-manifest/)
(page dated 2026-09-01) and [release manifest](https://developers.meta.com/horizon/resources/publish-mobile-manifest/)
(2026-08-31), rechecked 2026-09-21. **Development and release requirements are two different documents.**

## Contents

- Development manifest
- Release manifest (the one review enforces)
- SDK levels, with the 2026 rule
- Gradle and the OpenXR loader
- Supported devices and compatibility mode

## Development manifest

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="<packagename>">
  <uses-feature android:name="android.hardware.vr.headtracking"
                android:required="true" android:version="1" />
  <application android:label="@string/app_name"
               android:theme="@android:style/Theme.Black.NoTitleBar.Fullscreen">
    <activity android:name="android.app.NativeActivity"
              android:screenOrientation="landscape"
              android:configChanges="density|keyboard|keyboardHidden|navigation|orientation|screenLayout|screenSize|uiMode"
              android:excludeFromRecents="false">
      <intent-filter>
        <action   android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
        <category android:name="com.oculus.intent.category.VR" />
      </intent-filter>
    </activity>
  </application>
</manifest>
```

- `android.hardware.vr.headtracking` `required="true"` is also what v2 signing
  and store review expect from an immersive app.
- **Never** add `android:noHistory`.
- Landscape and the black fullscreen theme are comfort requirements during app
  transitions, not style.

## Release manifest — the delta

| Element | Release requirement |
|---|---|
| `android:debuggable` | `false` or absent — a release build |
| `installLocation` | `auto` (or `0`); anything else needs store-team approval |
| `android:label` | the app's name, **unique on the platform** |
| `android.hardware.vr.headtracking` | `required="true"` for immersive; omitted or `false` for a 2D panel app |
| `android:excludeFromRecents` | `true` in the release launch activity |
| intent filter | `MAIN` + `LAUNCHER`; current Meta OpenXR release example adds `com.oculus.intent.category.VR` |
| `com.oculus.supportedDevices` | `quest2\|questpro\|quest3\|quest3s` as a `meta-data` element in `application` |

The snippet is a manifest segment, not a complete generated project. Verify
merged APK output and preserve additional categories required by the chosen
SDK/cross-runtime target; the Meta category is not a universal OpenXR spec rule.

Non-conformance fails `VRC.Quest.Packaging.1` and/or `.4` — while still
installing happily when sideloaded, which is what makes it a late surprise.

## SDK levels, with the 2026 rule

Recommended for in-lifecycle devices (Quest 2, Quest Pro, Quest 3 family):

| | minSdkVersion | targetSdkVersion | compileSdkVersion |
|---|---|---|---|
| Recommended | 32 | 34 | 34 |
| Legal range | 29–34 | 32–34 immersive, 32–36 for 2D | ≥ targetSdkVersion |

**Apps created since 1 March 2026 must set `targetSdkVersion` to 34.** Horizon
OS has been Android 14 (SDK 34) since HzOS v76 in April 2025; older releases
were Android 12 (SDK 32). To gate on a Horizon OS version rather than an Android
one, use "Requiring Minimum OS Versions"
(`documentation/native/min-os-versions`), not `minSdkVersion`.

`maxSdkVersion` is supported by Android and **not recommended** on Quest.

## Gradle and the OpenXR loader

```gradle
android {
  compileSdk 34
  defaultConfig { minSdk 32; targetSdk 34; ndk { abiFilters 'arm64-v8a' } }
  buildFeatures { prefab true }          // required for the loader's prefab
  externalNativeBuild { cmake { cppFlags '-std=c++20' } }
}
dependencies {
  implementation 'org.khronos.openxr:openxr_loader_for_android:<version>'
}
```

- Only `arm64-v8a` ships: `VRC.Quest.Packaging.6` requires 64-bit binaries.
- **Loader below 1.0.34 crashes**; apps on the Khronos loader also crash on
  Horizon OS older than v62, and non-Quest-1 users below v62 never see the
  update in the Store.
- Pin the loader version in whatever lock file the project keeps **and** in
  `build.gradle`, then check they agree — a drifted lock is a release note
  describing a build that does not exist.

## Supported devices and compatibility mode

A headset whose model is absent from `com.oculus.supportedDevices` runs the app
in **compatibility mode** and reports itself as a previous generation. That is a
safety net, not a plan: query capabilities (extension enumeration) rather than
device models, and add new identifiers as they appear.
