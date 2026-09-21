# npm release automation — 2026-09-21

## Objective and scope

Make `@ssheleg/xr-dev` publish automatically from the existing family release
trigger: push a `vX.Y.Z` tag after its commit has reached the default branch.
Ordinary branch pushes run validation; they do not choose a package version.
The operator authorized npm setup and publication in this task. Keep the current
agent/model; no independent agent delegation or scheduled work is required.

## Requirements and acceptance

| Requirement | Evidence required |
|---|---|
| Bootstrap the unpublished package | Registry serves exact 0.3.0; CLI account authenticated |
| Configure GitHub trusted publishing | Trust names ssheleg/xr-dev and release.yml, direct publish allowed |
| Demonstrate unattended release | Tag-push run publishes a new 0.3.1 with provenance; publish step must not skip |
| Update family distribution | Parent pin/catalog/site/npm release agree; pending npm marker removed only after registry verification |
| Durable handoff | Owning branches pushed, checks and next task recorded |

## Source ledger and decisions

- Baseline: [release workflow](https://github.com/ssheleg/xr-dev/blob/6a5053253f45916937bde0972e5cae4bcee57007/.github/workflows/release.yml).
- [Previous release evidence](../../verification/2026-09-21-lifecycle/README.md).
- [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/), read 2026-09-21: GitHub-hosted runner, Node 24, modern npm and OIDC id-token permission. Explicitly allow direct publishing; new connections otherwise default to staged publishing.
- [npm trust CLI](https://docs.npmjs.com/cli/v11/commands/npm-trust/), installed npm 11.19.1 help read 2026-09-21: package must already exist and account 2FA is required. Configure with `npm trust github @ssheleg/xr-dev --repo ssheleg/xr-dev --file release.yml --allow-publish --yes`.
- Repository CLAUDE.md and docs/AGENT_SYNC.md: version synchronization, local advisory coordination, required checks and parent pin.
- Local npm login succeeded as ssheleg on 2026-09-21; initial publish requested separate account authentication. No credential belongs in Git.

## Plan and dependencies

1. Bootstrap 0.3.0 and configure trust (depends on npm account authentication).
2. Normalize package repository metadata, make OIDC explicit in the existing workflow,
   document release/recovery and bump all version metadata to 0.3.1.
3. Run repository gates, merge by PR, push v0.3.1; verify actual CI publication.
4. Advance the family pin and registry availability flag; release and verify the
   family site and installer. Preserve concurrent work in the umbrella.

## Progress and resume

Preparation: worktree based on 6a5053253f45916937bde0972e5cae4bcee57007;
no release-automation change implemented yet. Exact next task: complete bootstrap
account authentication, then configure trust and execute steps 2–4 above.

## Implementation checks

- Local gates passed: `npm test` (11 checks, 7 skills, 25 references),
  `npm run test:negatives` (8 planted defects caught), `node test/installer_test.js`
  (11 cases; all temporary homes removed), both strict Claude plugin validators.
- Initial publication printed `+ @ssheleg/xr-dev@0.3.0`; exact registry serving
  remains a separate propagation check, still 404 at 13:21 UTC.
- `npm trust list @ssheleg/xr-dev --json` returned GitHub `ssheleg/xr-dev`,
  `release.yml`, permissions `createPackage` and `createStagedPackage`.
  Direct publish is enabled; no npm secret is stored in GitHub.
- Remaining: observe actual 0.3.1 tag-push publication and finish umbrella propagation.

## Completed member delivery

- [PR 2](https://github.com/ssheleg/xr-dev/pull/2) merged; v0.3.1 points to
  `7515a914ce4aad860b5fd08ce472509d6f7f5bbf`.
- [Tag-push release run](https://github.com/ssheleg/xr-dev/actions/runs/35605315535)
  succeeded. The `npm publish` step actually ran, signed GitHub provenance and
  printed `+ @ssheleg/xr-dev@0.3.1`; the registry-serving check passed.
- Registry readback returned version 0.3.1 and integrity
  `sha512-xNnVAdjN8oPpPvEBRIzsgzraTRRa1Tt08SLKV1OPBKwbj1NEzGZgNsJ0kXdMsfJP1Sur86etgfM7B2t0QSusTw==`.
  [Registry provenance](https://registry.npmjs.org/-/npm/v1/attestations/@ssheleg%2fxr-dev@0.3.1)
  identifies a SLSA v1 statement.
- `RELEASE_ENABLED` and `PUBLISH_NPMJS` are true; GitHub repository secret listing
  is empty. Trust readback permits direct publishing from release.yml.
- Member resource claims released. Local-only credentials and cache state are not committed.

Remaining work belongs to [family PR 149](https://github.com/ssheleg/sshlg-skills/pull/149):
release family 1.51.1, verify site/package/installation and finish the central receipt.
[Central handoff](https://github.com/ssheleg/sshlg-skills/blob/codex/xr-npm-family/docs/evidence/releases/2026-09-21-xr-npm/README.md).
The next member release requires the normal version bump, merged commit and tag push;
it no longer requires npm login or a manual publish.
