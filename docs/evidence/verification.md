# Verification evidence — xr-dev

## Release candidate: v0.4.5 (2026-10-28)

quest-store and quest-tooling advertise forms that name the headset. Evidence: the repository gate exits 0 on the candidate tree; the PR CI run
and the tag release run are named in docs/HANDOFF.md.

## Release candidate: v0.4.4 (2026-10-25)

descriptions within a 300-character budget. Evidence: the repository gate exits 0 on the candidate tree; the PR CI run
and the tag release run are named in docs/HANDOFF.md.

## Release candidate: v0.4.3 (2026-10-24)

the family member gate. Evidence: the repository gate exits 0 on the candidate tree; the PR CI run
and the tag release run are named in docs/HANDOFF.md.

## Release candidate: v0.4.2 (2026-10-22)

the ledger records the shipped version

Evidence: `npm test` exit 0 on the candidate tree before the PR; the PR CI run and the tag release run are named in docs/HANDOFF.md.

## v0.4.0: short router descriptions (2026-10-20)

| Evidence needed | Owning source | Scope and limits |
|---|---|---|
| Description lengths and the 500-char cap | `test/validate.py` (`npm test`, `npm run test:negatives`, both exit 0 on the candidate) | Structure only. No model routing quality is claimed. |
| Every routed trigger still in the skill text | A scratch check over the umbrella's routing table: 53 triggers, 0 missing from the SKILL.md text, 18 now only in a body `## Triggers` section | Until the umbrella's own check reads the whole SKILL.md, it reports those 18 as unadvertised. |

## v0.3.4 — published-source evidence index (2026-10-13)

This index makes existing owner evidence discoverable. It does not re-run or
re-stamp historical checks. The version identifies the artifact in the linked
publication receipt; the repository also contains documented, payload-preserving
successors. A matching family-ledger heading is not a new acceptance result.

| Evidence needed | Owning source | Scope and limits |
|---|---|---|
| Release and publication | [Release packet](releases/2026-10-13-member-gates/README.md#published-readback) and [machine readback](releases/2026-10-13-member-gates/published-readback.json) | Exact original tag/source, release run, registry integrity and packaged-file hashes. Preserve the receipt's date and source. |
| Board and release safeguards | [Implementation and witnessed controls](member-gates-20261013/README.md) | Bounded source/process validation, including its intermediate failures; not a general YAML/Bash proof. |
| Repository-only successor | [Shared-header correction](member-gates-headers-20261013.md) and [owner board](backlog.md) | Declared source/payload preservation and publication reconciliation; no new package release. |
| This index change | [FW00 packet](fw00-verification-index-20261013/README.md) | Link/version discovery and unchanged package evidence only; current checks are recorded separately from historical receipts. |

Installed host discovery, native hooks, model task quality and live provider/device
behavior are **not established by this index**. Read their own source-bound receipts
if needed; package equality does not imply them. Older runs keep their original
confirmation state. No human confirmation or completed pipeline run is invented.

[Current handoff](../HANDOFF.md) names the next task.
