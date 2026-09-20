# Security

## Reporting

Report anything sensitive privately to **security@sshlg.me**, not in a public
issue. Include the file, what happens, and what you expected.

## What executes when you install this

| Path | Runs when | What it touches |
|---|---|---|
| `bin/xr-dev.js` | `npx @ssheleg/xr-dev` | copies the skill directories into `~/.claude/skills/<name>`; refuses (exit 3) when the plugin is already installed; writes nothing else |
| `install.sh` | run by hand | the same copy, in POSIX shell |
| `test/*.py`, `test/*.js` | only in CI or by hand | read the repository; `check_schemas.py` makes outbound HTTPS requests to schemastore.org |

The skills themselves ship **no hooks, no MCP server and no background
process**. Nothing here runs at session start.

## What the skills tell an agent to run

The bodies name `metavr`, `adb`, `keytool`, `bubblewrap`, `npm` and `git`
commands. Two classes deserve attention before an agent runs them unattended:

- **Device-mutating**: `metavr app install|uninstall`, `metavr files rm`,
  `metavr device configure-testing`, `metavr shell`. They act on a connected
  headset.
- **Outward-facing**: `metavr store dist upload` and `copy-build` put a build in
  front of testers or the Store. Uploads default to a **draft**; `--publish` is
  the flag that makes it visible. Treat both as actions needing a human's say-so.

No skill asks an agent to bypass a consent prompt, and no skill fetches its own
instructions from a URL at runtime.

## Credentials

Nothing in this repository stores or reads a credential. `metavr auth login`
keeps its token in the OS keychain; `METAVR_TOKEN` exists for CI. Signing
keystores belong outside the repository, and every skill that mentions one says
so.
