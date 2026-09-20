# CLAUDE.md — xr-dev

House rules for **this repository only**. Family doctrine (language, quality bar,
routing) loads from `~/.claude/CLAUDE.md` in the same session; a second copy here
would be a second source of truth that drifts.

## What this repo is

Five agent skills for Meta Quest and Horizon OS, separated by **the question
being answered** rather than by the tool that answers it. A tool skill ages with
the tool; a question skill ages with the platform, and Horizon OS moves on its
own cadence.

Meta publishes 29 task skills of its own, twelve of them Unity-specific. **This
pack never duplicates them.** Where Meta owns the lane — Unity, a specific
profiler's flags, the Spatial SDK — the body routes there by name.

## The gate

```bash
npm test               # test/validate.py: structure, version sync, budgets, references, links
npm run test:negatives # plant each defect and require the validator to refuse it
node test/installer_test.js
claude plugin validate . --strict && claude plugin validate plugins/xr-dev --strict
```

All green or the change does not land.

## Invariants — each one has a check that has been watched failing

- **Every fact carries its receipt.** A number, a flag, a requirement: quoted
  with the page it came from and the date it was read. A claim from memory about
  a Quest API is a bug, because the reader cannot tell it from a measured one.
- **The VRC reference is generated, not transcribed** — the script that writes
  it counts what it wrote (80 requirements, 14 groups). A hand-typed count is an
  assertion that drifts the release after it is written.
- **A body names every reference it ships, and ships every reference it names.**
  The validator checks both directions: a reference that stopped shipping reads,
  to an agent, exactly like one that never existed.
- **Descriptions keep the 60-character reserve** below the 970 house cap. The
  family ratchets that count; the room exists for the "NOT for" clause the next
  neighbouring skill will force.
- **Prose is English.** Russian survives only inside trigger phrases, where the
  string itself decides whether the skill fires.

## Coordination

`docs/AGENT_SYNC.md` — generated from `.claude/agent-sync.json`, describing how
coordination is wired here and which files are guarded. Regenerate with
`agent_sync.py setup`; never hand-edit it.

## Releasing

Bump the version in all five places at once (marketplace.json, plugin.json,
package.json, the CHANGELOG entry, each `SKILL.md` `metadata.version`) — the
validator enforces it. Then tag, push the tag, and move the family submodule pin
in `ssheleg/sshlg-skills` in the same session: a member released without its
umbrella pin bumped is invisible to everyone who installs through the family.
