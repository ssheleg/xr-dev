# The VRC list, as read on 2026-09-20

**Read this when** preparing a submission or explaining a rejection. This is a
snapshot of `resources/publish-quest-req` (page dated at the source) taken on
2026-09-20 — requirements retire and appear, so **fetch the live page before a
submission**:

```bash
metavr docs fetch resources/publish-quest-req.md
```

Legend, as Meta uses it: **✓** required, **+** recommended (a "plus"), **N/A**
not applicable. Two columns because immersive and 2D panel apps are judged
differently. RETIRED entries are omitted here; their numbers are not reused.

## Contents

- Packaging
- Audio
- Performance
- Functional
- Security
- Tracking
- Input
- Asset
- Ads
- Accessibility
- Streaming
- Privacy Policy
- Content
- Publishing

## Packaging

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Packaging.1` | The application manifest must conform to release build manifest requirements. | ✓ | ✓ |
| `VRC.Quest.Packaging.2` | You must sign your app with APK signature scheme v2. | ✓ | ✓ |
| `VRC.Quest.Packaging.3` | Your app must not require Android features not supported on Quest. | ✓ | ✓ |
| `VRC.Quest.Packaging.4` | You must use a supported SDK and engine version. | ✓ | ✓ |
| `VRC.Quest.Packaging.5` | APK file size must be less than 1 GB. OBB files must be less than 4 GB. | ✓ | ✓ |
| `VRC.Quest.Packaging.6` | All Quest applications must be submitted as 64-bit binaries. | ✓ | ✓ |

## Audio

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Audio.1` | Apps should support 3D audio spatialization, although it is not required. | + | + |

## Performance

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Performance.1` | The app must run at the specified refresh rates. | ✓ | + |
| `VRC.Quest.Performance.3` | The app must either display head-tracked graphics in the headset within 4 seconds of launch or provide a loading indicator in VR. | ✓ | + |
| `VRC.Quest.Performance.4` | The app should run at no less than 85% render scaling for the majority of the experience. | + | N/A |

## Functional

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Functional.1` | App must install and run without crashes, freezes, or extended unresponsive states. | ✓ | ✓ |
| `VRC.Quest.Functional.2` | Single player apps must pause when the Horizon OS requests the app to pause. | ✓ | + |
| `VRC.Quest.Functional.3` | The app must not leave the user stuck at any point in the experience. | ✓ | ✓ |
| `VRC.Quest.Functional.4` | The app must not lose the user's data. | ✓ | ✓ |
| `VRC.Quest.Functional.5` | The application must respond to the headset positional tracking as well as orientation. | ✓ | ✓ |
| `VRC.Quest.Functional.6` | App must only include Meta Quest headsets and controllers within the title or Store assets. | ✓ | ✓ |
| `VRC.Quest.Functional.7` | If your app requires Internet connectivity for its core functionality, notify users without an active Internet connection that one is required. | + | + |
| `VRC.Quest.Functional.9` | In experiences using a Local tracking space, the user must be able to reset their forward orientation. | ✓ | N/A |
| `VRC.Quest.Functional.10` | Headlocked menus and UI elements are generally uncomfortable for the user and should be avoided. | + | N/A |
| `VRC.Quest.Functional.12` | Apps must run correctly and with full functionality for multiple entitled users on the headset. | ✓ | ✓ |
| `VRC.Quest.Functional.13` | Apps that support localization must default to the user's configured language and default to English if the app doesn't support that language. | + | + |
| `VRC.Quest.Functional.14` | Apps that can launch directly in passthrough should show passthrough loading screens and launch in passthrough when the user is coming from MR Home. | ✓ | + |

## Security

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Security.1` | The app should perform a Platform entitlement check within 10 seconds of launch. | + | + |
| `VRC.Quest.Security.2` | The app must request the minimum number of permissions required to function and may not include permissions that are unsupported. | ✓ | ✓ |

## Tracking

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Tracking.1` | When configuring the submission metadata for your app, it must meet the requirements for either sitting, standing, or roomscale play modes. | ✓ | N/A |
| `VRC.Quest.Tracking.2` | When configuring the submission metadata for your app, it must meet the requirements for the supported input modes that you select. | ✓ | ✓ |

## Input

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Input.1` | In-game menus should be activated with the menu button on the gamepad controller or the menu button on the left Touch controller. | + | + |
| `VRC.Quest.Input.2` | When picking up objects within the app, use the Touch controller's grip button rather than the trigger button. | + | N/A |
| `VRC.Quest.Input.3` | In-application hands and controllers should line up with the user's real-world counterparts in position and orientation as closely as possible. | + | N/A |
| `VRC.Quest.Input.4` | Apps must be focus-aware. They must continue rendering when they lose focus, hide any user hands or controllers, and ignore all input. | ✓ | N/A |
| `VRC.Quest.Input.5` | For applications that support hand tracking, hands must render in the correct position and orientation, and must animate properly. | + | N/A |
| `VRC.Quest.Input.7` | For applications that support hand tracking, the application must properly respect when input is switched between controllers and hands. | ✓ | ✓ |
| `VRC.Quest.Input.8` | For applications that support hand tracking, the system gesture is reserved, and should not trigger any other actions within the application. | ✓ | ✓ |

## Asset

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Asset.1` | Logo must be on a transparent background. | ✓ | ✓ |
| `VRC.Quest.Asset.2` | Store cover art images must have clear branding without extraneous text, taglines, or banners | ✓ | ✓ |
| `VRC.Quest.Asset.3` | Store cover art should not include text in the top or bottom 20% of the image. | + | + |
| `VRC.Quest.Asset.4` | Hero art must include the branding and/or title of the app centered in the image. | + | + |
| `VRC.Quest.Asset.5` | Screenshots must be representative of the app and don't contain any additional logos, text, or iconography. | ✓ | ✓ |
| `VRC.Quest.Asset.6` | App description, screenshots, and videos must not include headsets, controllers, or logos for other VR platforms. | ✓ | ✓ |
| `VRC.Quest.Asset.7` | Trailer must not be longer than 2 minutes. | ✓ | ✓ |
| `VRC.Quest.Asset.8` | Artwork asset text should not use a font smaller than 24 pt. | + | + |
| `VRC.Quest.Asset.9` | If using Immersive Image Layers, Immersive Object Left, Immersive Object Right, and Immersive Logo images must be on a transparent background. | ✓ | ✓ |
| `VRC.Quest.Asset.10` | All screenshots or trailers that showcase Meta Quest Pro exclusive functionality must include the text “Captured on Meta Quest Pro.” | + | N/A |

## Ads

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Ads.1` | The app must meet all advertising policy requirements. | ✓ | ✓ |
| `VRC.Quest.Ads.2` | Ad supported apps must include the ‘Contains Ads’ label on the Product Details Page. | ✓ | ✓ |
| `VRC.Quest.Ads.3` | Ads cannot be stereoscopic, head-tracked, or immersive. | ✓ | ✓ |
| `VRC.Quest.Ads.4` | Ads which interfere with app use must provide a clear method for dismissal. | ✓ | ✓ |
| `VRC.Quest.Ads.5` | Ads which interfere with app use cannot be placed after each of consecutive user actions. | ✓ | ✓ |
| `VRC.Quest.Ads.6` | Ads cannot impair device functionality. | ✓ | ✓ |
| `VRC.Quest.Ads.7` | Ads cannot facilitate inadvertent clicks from users, for example by mimicking Horizon OS notifications and features or elements of the app’s UI which users would not reasonably expect to be associated with ads. | ✓ | ✓ |

## Accessibility

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Accessibility.1` | The app should be playable without audio. | + | + |
| `VRC.Quest.Accessibility.2` | Text and in-app controls and elements necessary for app progression should be clearly legible. | + | + |
| `VRC.Quest.Accessibility.3` | The app should provide clarity and direction to the user through a combination of visual, audio, and/or haptic feedback when possible. | + | + |
| `VRC.Quest.Accessibility.4` | The app should provide an option to be played with one hand and/or controller. | + | + |
| `VRC.Quest.Accessibility.5` | The app should enable people to edit their display settings such as brightness and contrast to accommodate their visual needs. | + | + |
| `VRC.Quest.Accessibility.6` | The app should either provide color blindness options, or use other techniques such as combining color and pattern for easy visual distinction. | + | + |
| `VRC.Quest.Accessibility.7` | The app should provide the user with the option to rotate their view without physically moving their head/neck. | + | + |
| `VRC.Quest.Accessibility.8` | The app should support multiple locomotion styles when possible. | + | + |
| `VRC.Quest.Accessibility.9` | Applications that can be used in sitting or standing mode should provide a setting to enable users to perform all interactions and access information from a fixed position. | + | N/A |

## Streaming

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Streaming.1` | Applications that stream stereoscopic, head-tracked, or immersive content must handle user connectivity issues in a graceful manner. | + |  |
| `VRC.Quest.Streaming.2` | Applications that stream stereoscopic, head-tracked or immersive content may only do so from a local PC that the customer has physical access to, unless expressly approved by Meta. | ✓ |  |
| `VRC.Quest.Streaming.3` | Applications that stream stereoscopic, head-tracked or immersive content from virtual devices or cloud sources must display  connectivity notices. | ✓ |  |
| `VRC.Quest.Streaming.4` | Apps that stream stereoscopic, head-tracked or immersive content from virtual devices or cloud sources must not be directed at children under the age of 13. | ✓ |  |

## Privacy Policy

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Quest.Privacy.1` | Privacy Policy URL links to a privacy policy statement managed by the app’s team. | ✓ | ✓ |
| `VRC.Quest.Privacy.2` | Privacy Policy has a clear explanation of what data the app is collecting about the user. | ✓ | ✓ |
| `VRC.Quest.Privacy.3` | Privacy Policy has a clear explanation of how the app is using user data. | ✓ | ✓ |
| `VRC.Quest.Privacy.4` | Privacy Policy has a clear explanation of how the user may request that their user data that has been collected or stored can be deleted. | ✓ | ✓ |
| `VRC.Quest.Privacy.5` | Team and app must clear data protection checks. | ✓ | ✓ |

## Content

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Content.1` | The app must meet all content guidelines. | ✓ | ✓ |
| `VRC.Content.2` | App metadata must match the app's in-app content. | ✓ | ✓ |
| `VRC.Content.3` | Apps with user-generated content must have a form for users to notify the developer about conduct in the application that does not adhere to the Code of Conduct. | ✓ | ✓ |
| `VRC.Content.4` | Apps with user-generated content should provide the user with a way to immediately hide undesired content. | + | + |

## Publishing

| VRC | Requirement | Immersive | 2D |
|---|---|---|---|
| `VRC.Publishing.1` | App website URL must link directly to a valid page. | ✓ | ✓ |
| `VRC.Publishing.2` | If present, External Support Link URL must link directly to a valid support page. | ✓ | ✓ |
| `VRC.Publishing.3` | If present, Terms of Service (TOS) URL must link directly to a valid TOS page. | ✓ | ✓ |
| `VRC.Publishing.4` | The app's Name must meet all content guidelines. | ✓ | ✓ |
| `VRC.Publishing.5` | The app's Short Description must meet all content guidelines. | ✓ | ✓ |
| `VRC.Publishing.6` | The app's Long Description must meet all content guidelines. | ✓ | ✓ |
| `VRC.Publishing.7` | Search Keywords must be relevant to the app and meet all content guidelines. | ✓ | ✓ |
| `VRC.Publishing.8` | Any use of the Meta brands in app metadata must meet Brand Guidelines. | ✓ | ✓ |

## How to use it without drowning

1. Packaging and Security first — they are binary, cheap to check, and they are
   what an automated pass rejects.
2. Performance and Functional next — they need a real headset and a real
   session, so they gate the release candidate rather than the branch.
3. Assets last, but not late: they fail more submissions than code does, and
   fixing them means re-exporting art, not editing a line.

Each id has its own page with the test steps: `resources/vrc-quest-<group>-<n>`,
for example `resources/vrc-quest-packaging-2`.
