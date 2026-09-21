# Store asset production and review

**Read this when**: before capture, listing design or submission. Read the current
[asset specification](https://developers.meta.com/horizon/resources/asset-guidelines/)
and [marketing-material policy](https://developers.meta.com/horizon/resources/store-marketing-materials/)
for the app category and region. Inspected 2026-09-21; verify again before export.

## Build a checked asset manifest

Use `docs/xr/asset-manifest.json` or an existing production catalog. Each item names
purpose, source build/capture, editable master, export path/hash, rights/consent,
locale, dimensions/format, validation and reviewer. Separate required Store assets,
optional previews, press kit and social/ad variations. Do not bake every current
pixel dimension into an undated prompt; fetch the actual table and crop templates.

The inspected specification requests five distinct actual-experience screenshots,
with limited MR/third-person exceptions. Key art/title consistency, safe areas,
format/alpha, icon shape and preview/trailer rules need separate checks. Its
spatialized-icon transparency wording conflicts with its general PNG-alpha note;
confirm that asset type in Dashboard/template rather than silently normalizing it.

## Production loop

1. Product/UX establishes the promise; copywriting reads the brand pack; design
   creates a coherent master with separate background, subject and exact title.
2. Capture a reproducible representative build with a shot list, stable camera,
   legible action, controlled notifications/debug UI and appropriate audio tracks.
   Protect player names, room imagery, voices and licensed music.
3. Keep gameplay evidence truthful. Generative tools may create concepts or approved
   key-art derivatives; never fabricate a gameplay screenshot or claim a universal
   percentage of AI video is permitted. Check each asset against its actual use.
4. Export each surface from editable masters. Inspect safe zones at small thumbnail
   size and across crops, plus title/locale parity, visible compression and audio.
   Tool-reported dimensions alone do not prove that the title remains readable.
5. Run file/dimension/codec checks with available media tools; use the Dashboard
   preview and review actual pixels. Cropping/asset-library/AI expansion helpers
   can assist production, but they do not certify truthful content or approval.
6. Keep technical acceptance and visual/policy review distinct. Pass assets to
   quest-store with their evidence, then plan controlled PDP creative experiments.

Use [Meta's production guide](https://developers.meta.com/horizon/resources/gtm-marketing-assets/)
for capture/repurposing and [marketing plan](https://developers.meta.com/horizon/resources/gtm-marketing-plan/)
for audience/CTA/channel decisions. Reuse its linked worksheets/templates when
accessible; do not claim their contents were verified if login blocks access.
Foundry manages jobs/provenance, Blender creates editable scene assets, media tools
compose footage and the engine supplies gameplay proof. No companion: do these
steps with ordinary files and installed capture/export tools; missing capture
hardware leaves source-gameplay verification NOT_RUN.
