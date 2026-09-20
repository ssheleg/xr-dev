# Capture playbook — the exact sequences

**Read this when** a performance problem needs evidence rather than an opinion,
or when a capture has to be handed to another agent or another person.

Commands verified against `metavr` 1.3.2.2.2 on 2026-09-20 (`metavr perf --help`
and its subcommands). Every one of them needs a **connected headset**; a
simulator answers behaviour questions only.

## Contents

- Step 0: the numbers before any tool
- Perfetto through metavr
- simpleperf: CPU hotspots and what is actually bound
- RenderDoc: the GPU side
- OVR Metrics Tool: live, in the headset
- What a usable capture report contains

## Step 0: the numbers before any tool

```bash
metavr device list                  # the headset is attached at all
metavr device battery               # a throttling device invalidates the run
metavr app launch <package>
metavr log | grep -E 'FPS=|Stale=|App='
```

Read `App` (ms) against the refresh-rate budget, `Stale` against the refresh
rate, and only then `GPU%`. The interpretation — including why `GPU%` reads low
exactly when the app is GPU-bound — is in the skill body.

## Perfetto through metavr

```bash
# one-shot, fixed duration
metavr perf capture --mode vr --duration 10000 --app <package> -o before

# or bracket an interaction by hand
metavr perf start --mode custom --gpu-render-stage --cpu-scheduling --xr-runtime
#   … reproduce the worst scene in the headset …
metavr perf stop

metavr perf analyze-trace --focus frames        # overview | gpu | cpu | frames | threads
metavr perf compare before after                # a delta report, after one change
metavr perf open                                # ui.perfetto.dev, for a human
metavr perf query "<SQL>"                       # trace processor, for a specific question
```

Modes: `standard`, `gpu`, `cpu`, `lightweight`, `full`, `vr`, `custom`. Start
with `vr`; go to `custom` when a specific data source is missing. The `--gpu-*`,
`--cpu-scheduling`, `--xr-runtime` and `--vulkan-layer` switches only apply to
`custom`.

Meta's `hz-perfetto-debug` skill drives this tool in depth — use it once the
capture exists.

## simpleperf: CPU hotspots and what is actually bound

```bash
metavr perf simpleperf classify          # CPU-bound, memory-bound or I/O-bound, from PMU counters
metavr perf simpleperf record            # cycle-sampled hotspots
metavr perf simpleperf kernel-overhead   # kernel vs userspace, per thread
```

`classify` first: optimising a memory-bound loop as if it were compute is the
most common wasted day. Meta's `hz-simpleperf-debug` covers the deeper flags.

## RenderDoc: the GPU side

`metavr tools install renderdoc` (Meta's fork). Three captures answer three
different questions:

| Question | Capture |
|---|---|
| Which draw call costs what | draw-call trace |
| Which render stage dominates | render-stage trace |
| Is a shader the problem | Vulkan shader stats |

Docs: `ts-renderdoc-for-oculus`, `ts-renderdoc-capture`, `ts-renderdoc-drawcall`,
`ts-renderdoc-renderstage`, `ts-renderdoc-shaderstats`.

## OVR Metrics Tool: live, in the headset

`metavr tools install ovrmetric` installs the OVRMonitorMetricsService APK;
enable its overlay on the device to watch FPS, stale frames and utilisation
while playing. Best for "does this scene ever recover", worst for precise
numbers — the overlay itself costs a little.

## What a usable capture report contains

A report another agent can act on names all seven:

1. build id and whether it is a **release** build;
2. device model and Horizon OS version;
3. requested refresh rate, and therefore the budget in ms;
4. the scene and the interaction reproduced;
5. `App` ms, `Stale`, `FPS=x/y`, `GPU%` — as read, not summarised;
6. battery/thermal state at capture time;
7. the trace file path, so the claim can be re-checked.

A performance claim missing (1), (3) or (7) cannot be verified later and will
be re-measured from scratch.
