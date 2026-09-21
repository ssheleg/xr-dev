# Releasing xr-dev

## Automatic path

[release.yml](../.github/workflows/release.yml) runs on a pushed `v*` tag or a
manual dispatch naming an existing tag. It calls the validation workflow, checks
that the tag is reachable from the actual default branch, checks manifest versions,
creates/refreshes the GitHub release, installs the GitHub package in a clean home,
and publishes the npm package with provenance. GitHub OIDC authenticates publishing;
there is no `NPM_TOKEN` dependency. Node 24 and current npm run on GitHub-hosted Ubuntu.

Repository variables `RELEASE_ENABLED=true` and `PUBLISH_NPMJS=true` enable the two
release jobs. They are deliberately opt-in for forks. A normal branch push runs
validation; it does not invent or bump the release version.

1. Update package.json, marketplace manifest, plugin manifest, all skill metadata
   versions and CHANGELOG.md together. Run the checks in [CLAUDE.md](../CLAUDE.md).
2. Merge the tested change through the repository's PR policy.
3. Tag that exact merged commit and push the tag (`git tag -a vX.Y.Z <commit> -m
   "vX.Y.Z"`, then `git push origin vX.Y.Z`; replace placeholders with the release).
4. Verify the Actions publish step actually ran, then check `npm view
   @ssheleg/xr-dev@X.Y.Z version dist.integrity dist.attestations --json`.
5. Advance the xr-dev submodule and catalog in ssheleg/sshlg-skills, release the
   umbrella, verify its site/npm payload and use `npx sshlg-skills update`.

## One-time npm setup

The package must exist before configuring trust. The maintainer needs package write
access and account 2FA. First publish an already-tested release from an authenticated
CLI (`npm login`, `npm publish --access public`) and complete npm's browser challenge.
Then, with npm >=11.15.0:

```bash
npm trust github @ssheleg/xr-dev --repo ssheleg/xr-dev --file release.yml --allow-publish --yes
npm trust list @ssheleg/xr-dev --json
```

Complete npm's 2FA challenge. The trust must name the exact owner, repository and
workflow filename, with **publish** permission. New trust connections can default
to staged publishing, so direct `npm publish` requires explicit permission.
`repository.url` must identify this GitHub repository. Do not copy an npm token from
another project's secret or disable account 2FA to make a release pass.

References checked 2026-09-21: [npm trusted publishers](https://docs.npmjs.com/trusted-publishers/)
and [npm trust](https://docs.npmjs.com/cli/v11/commands/npm-trust/).

## Recovery and proof

- Failed validation: correct the source and release a new version; do not move an
  existing published tag or overwrite an npm version.
- Authentication failure: inspect trust permissions/repository/workflow and the
  job's `id-token: write` permission. `npm whoami` is a local-account check, not
  a CI OIDC health check. Keep the actual publish result as evidence.
- A version already exists: rerun skips publishing safely. A green skipped job
  does **not** demonstrate OIDC; observe an unpublished version succeed instead.
- Registry propagation: the workflow checks the exact version for up to ten
  minutes. If publication succeeded but serving lagged, rerun the failed job.
- A failed run may be retried from Actions, or `gh workflow run release.yml
  --repo ssheleg/xr-dev --ref main -f tag=vX.Y.Z` for an existing eligible tag.

Record run URLs, tag commit, registry integrity, parent pin and remaining work in
[release evidence](evidence/releases/2026-09-21-npm-automation/README.md).
