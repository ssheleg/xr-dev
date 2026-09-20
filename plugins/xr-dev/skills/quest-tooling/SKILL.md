---
name: quest-tooling
description: >-
  Use when setting up or driving the Meta Quest toolchain on a development
  machine - the metavr CLI and its MCP server, Meta's agentic skills, connecting
  a headset, installing the managed tools (Perfetto, RenderDoc, OVR Metrics,
  platform-utils, XR Simulator), and working with no headset at all. Also the
  hygiene - one install channel per agent, and no skill copies in a repository. Triggers -
  "metavr", "metavr init", "Meta VR CLI", "Quest MCP" / "MCP для Quest",
  "connect the headset" / "подключить шлем", "adb to Quest" / "adb к шлему",
  "install the APK" / "поставить apk на шлем", "developer mode" / "режим
  разработчика", "XR Simulator" / "симулятор", "no headset" / "нет шлема",
  "which Quest tools are installed" / "что установлено для Quest",
  "hz- skills" / "скилы Meta". NOT for writing app code (quest-native), reading
  a capture (quest-perf), or submitting a build (quest-store).
license: MIT
metadata:
  version: 0.2.1
---

# The Quest toolchain: one CLI, two interfaces, one channel per agent

`metavr` (Meta VR CLI) is a single tool with two faces: a command line, and a
stdio **MCP server** an agent drives on its own. Everything below is available
through both — the CLI names are given because they are also the fallback when
no MCP server is configured.

## Install it once, through one channel

| Channel | Command | Updates |
|---|---|---|
| Native installer (preferred) | `curl -fsSL https://developers.meta.com/horizon/install-cli/ \| sh` → `~/.metavr/bin` | `metavr update`, in place |
| npx, no install | `npx -y metavr@latest <cmd>` | always current |
| npm global | `npm install -g metavr` | **never on its own** — needs `npm update -g metavr` |

Two of these installed at once is a version split waiting to be read as a bug:
on this estate `~/.metavr/bin/metavr` (1.3.2.2.2) and `/opt/homebrew/bin/metavr`
(npm 1.3.2) both answered to `metavr`, and PATH order decided which. Check with
`which -a metavr` and keep one.

Sign in — `metavr auth login`, verify with `metavr auth status`. It unlocks the
Store commands; `METAVR_TOKEN` covers unattended automation.

## `metavr init` is the trap, not the setup

`init` installs skills, configures MCP servers and installs agent plugins. With
**no target flag it means `--all-agents`**, and "all agents" is its own fixed
list, not the agents you have. Run inside a project directory it writes one
`skills/` tree per agent **into that directory**.

Measured 2026-09-20 in a game repository: 29 skills × 25 directories = **4129
files, 47 MB**, untracked, uncovered by `.gitignore` — and the next `git add -A`
committed the lot into the product.

```bash
metavr mcp install claude-code      # one agent, MCP only, global
metavr mcp install project          # .mcp.json in THIS directory — shareable, in-repo
metavr init --cursor --no-auth      # one agent, full setup, no browser step
```

Before any of them in a git repository: ignore the destinations first
(`.claude/skills/*`, `skills/`, `.agents/` and the per-agent dotdirectories),
then run.

## The command map

| Job | Command |
|---|---|
| What is attached | `metavr device list` / `device info <id>` / `device battery` |
| Pair over Wi-Fi | `metavr device connect` (USB first), `device wait`, `device health-check` |
| Make a device test-stable | `metavr device configure-testing` (animations off, stay awake) |
| Install / launch / stop a build | `metavr app install <apk>` / `app launch <pkg>` / `app stop <pkg>` |
| Logs | `metavr log` (logcat), `metavr shell <cmd>` |
| Screens | `metavr capture screenshot` |
| Files on device | `metavr files push` / `pull` / `ls` / `rm` |
| UI automation | `metavr ui dump` / `tap` / `type` / `swipe` / `wait` |
| Performance | `metavr perf capture` / `start` / `stop` / `analyze-trace` / `compare` / `simpleperf` |
| Docs and API reference | `metavr docs search` / `fetch` / `api-search` |
| 3D assets | `metavr asset search "<thing>"` |
| Store distribution | `metavr store dist apps` / `channels` / `upload` / `copy-build`; `store test-user` |
| Emulator | `metavr ssim` (SpatialSim) |
| Managed tools | `metavr tools list` / `install <name>` |
| Setup report | `metavr doctor` |

`metavr doctor` reports **installed software only** — it does not test device
connectivity, sign-in or MCP wiring. A green doctor with no headset attached is
still a machine that cannot run anything.

## The MCP server, and how it ends up registered twice

`metavr mcp server` is the stdio server. Two ways it reaches an agent:

1. **Meta's plugin** `meta-vr@meta-quest` — ships the MCP server *and* 29 agent
   skills. A plugin's MCP server has no per-server switch: enabling the plugin
   enables the server.
2. **A direct registration** in the agent's own config (global or per project).

Doing both gives one server two registrations and the agent two copies of every
tool (~37 each, measured on this estate). Pick one: the plugin if the skills are
wanted too, the direct registration if the native binary must be the one that
runs. The project-scoped form (`metavr mcp install project` → `.mcp.json`) is
the one that travels with the repository to another machine.

`metavr xroperator status` shows whether the XR Operator proxy is installed and
**federated into metavr's own MCP server** — when it is, a running XR app can be
inspected through the same connection; no second server to register.

## Meta's 29 skills, and what this pack adds

Meta publishes them at `github.com/meta-quest/agentic-tools` (plugin
`meta-vr@meta-quest`, also on `npx skills`, `gh skill`, Cursor, Codex, Gemini).
The split is worth knowing before wondering which one to reach for:

| Meta's skills | Count | Owner of the lane |
|---|---|---|
| `hz-unity-*` | 12 | Unity — this pack does not duplicate them |
| `hz-quest-verify-first`, `metavr-cli`, `portal` | 3 | doc verification and CLI reference |
| `hz-perfetto-debug`, `hz-simpleperf-debug`, `hz-vr-debug` | 3 | driving a specific profiler |
| `hz-store-submit`, `hz-store-pwa` | 2 | store mechanics |
| `hz-spatial-sdk`, `hz-iwsdk-webxr`, `hz-android-2d-porting`, `hz-platform-sdk`, `hz-psdk-integration`, others | 9 | other build paths |

This pack answers the questions that sit **above** a tool: which lane a project
is on, which number to read, what to measure, what the Store will reject. Where
a Meta skill drives the tool, use it — and say which one did the work.

## No headset on the desk

- `xrsim` (Meta XR Simulator) and `spatialsim` (`metavr ssim`) run app logic on
  the machine. They prove behaviour and integration.
- They **cannot** answer a performance question: no real GPU, no thermals, no
  compositor. See `quest-perf`.
- `metavr device browser <url>` and the Store test accounts
  (`metavr store test-user`) need a real device and an organization.

## Managed developer tools

`metavr tools install <name>` fetches and installs; `metavr tools list` shows
versions and what is present. What each is for — including which need a headset
— is in `references/tool-matrix.md`.

## Hygiene, because the estate pays for it later

1. **One channel per agent.** A plain copy under `~/.claude/skills/<name>` beats
   the plugin of the same name and serves its frozen version forever.
2. **Never vendor skills into a product repository.** They are installed on the
   machine; a repo copy is 47 MB of a third party's text your CI now lints.
3. Skills and plugins load at **session start** — restart the agent after
   changing either, or it keeps the old set.
4. After any install or removal, the check that must print nothing:

```bash
for d in ~/.claude/skills/*/; do n=$(basename "$d"); \
  [ -e ~/.claude/plugins/marketplaces/"$n" ] && echo "SHADOW: $n"; done
```

*CLI surface read from `metavr --help` at 1.3.2.2.2 on 2026-09-20; the install
and init behaviour was measured on this machine the same day.*
