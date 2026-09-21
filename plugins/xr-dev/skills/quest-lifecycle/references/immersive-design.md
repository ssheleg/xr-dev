# Immersive design acceptance

**Read this when**: before an interaction prototype or when a technically working build is hard
to use. Work from the product's UX scenarios; this reference supplies platform
questions and evidence, not a second visual-design authority. Checked 2026-09-21.

## Prototype in physical spaces

Choose the physical relationship: full VR, passthrough, bounded tabletop, room
adaptation or panel/immersive transition. Prototype first-use understanding,
placement, reaching, exit and recovery before producing final art. Test small and
large rooms, absent scene labels, low light/tracking loss, permission denial and
changed furniture. Scene/depth data are estimates, not a safety barrier. Query
current runtime support rather than hard-code an old overview's device list.

## Review against scenarios

| Area | Design decision | Evidence to request |
|---|---|---|
| Comfort and locomotion | Stable horizon, deliberate motion, teleport/snap alternatives where suitable, speed/vignette options, rest/exit affordance | Short sessions with intended users, symptom and task observations; headset removal/menu/focus tests |
| Input | Direct/ray/controller/hand alternatives; discoverable select/grab/release; system gestures respected | Same core task with supported inputs, loss/reacquisition and modality switches |
| Spatial layout | World/view/body anchoring chosen deliberately; avoid persistent intrusive head locking; distance and angular readability | Check near/far, seated/standing/recenter, occlusion, reach and sustained neck/arm effort |
| Accessibility | One-handed/seated alternatives, remapping where feasible, adjustable text/captions, color-independent cues and redundant feedback | Users and assistive modes, not a checklist alone; record unsupported paths |
| Audio/haptics | Spatial cues reinforce events; separate music/effects/voice controls; captions identify speaker/direction when needed | Hear/no-hear and haptics-disabled paths; intelligibility under real room noise |
| Display/materials | Stereo scale/depth consistency, linear/sRGB/alpha handling, readable panels and contrast against variable passthrough | On-device images and both-eye checks; screenshots alone cannot prove stereo comfort |
| Onboarding | Explain permission at use, teach one interaction at a time, quick meaningful success, resumable setup | First-time user completes the core task and can leave/recover unaided |

Specific distances, speeds, durations and text sizes in examples are starting
points for the chosen device/task, not blanket VRC thresholds. Keep requirements,
recommendations and your own hypotheses separate. Generic graphics-pipeline pages
may explain tessellation or mesh shaders without implying Quest support.

## Primary reading by question

- [Design hub](https://developers.meta.com/horizon/design/) and [MR introduction](https://developers.meta.com/horizon/design/mr-overview/): conceptual choices.
- [Key considerations](https://developers.meta.com/horizon/design/mr-design-guideline/): placement, input and spatial responsiveness.
- [Comfort](https://developers.meta.com/horizon/design/comfort/): motion and ergonomics.
- [Accessibility](https://developers.meta.com/horizon/design/accessibility/): controls, captions and testing.
- [Display](https://developers.meta.com/horizon/design/display/): stereo/depth and color management.
- [Scene design](https://developers.meta.com/horizon/design/mr-design-scene/): room-dependent experiences.

If hz-immersive-designer is installed, use it for deeper design review but verify
its numeric recommendations against current primary docs. Without it, execute the
table inline. No headset or representative users means comfort/usability remains
NOT_RUN; a desktop prototype still tests flow and state transitions.
