#!/usr/bin/env python3
"""Consistency gate for xr-dev. Stdlib only, offline.

What upstream gates do NOT see, and this one does:
  * `claude plugin validate --strict` reads MANIFESTS, never front matter;
  * the house rules (description shape, EN+RU triggers, budgets with headroom);
  * version sync across the five places a version is written;
  * references that ship and are named, in both directions.

`--self-test` plants one defect per guard in a copy of the tree and fails if
the guard stays green. A validator nobody has watched fail is decoration.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = "xr-dev"
PLUGIN_DIR = ROOT / "plugins" / PLUGIN
SKILLS_DIR = PLUGIN_DIR / "skills"

# Spec caps, and the house limits that leave room for the next edit (5%).
DESC_CAP = 1024
DESC_HOUSE = 970
BODY_LINES_CAP = 500
BODY_LINES_HOUSE = 475
BODY_TOKENS_CAP = 5000
BODY_TOKENS_HOUSE = 4750
# Deliberately pessimistic: cl100k gives 3.8-4.5 chars/token on English prose,
# so dividing by 3.6 over-counts rather than letting a body through at 101%.
CHARS_PER_TOKEN = 3.6

# Pinned, not pattern-matched: the address that was wrong looked exactly right.
SCHEMAS = {
    "marketplace": "https://json.schemastore.org/claude-code-marketplace.json",
    "plugin": "https://json.schemastore.org/claude-code-plugin-manifest.json",
}

SECRET_SHAPES = [
    re.compile(r"\bsk-[A-Za-z0-9]{16,}"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bOC[A-Za-z0-9]{20,}"),          # Oculus/Meta app secrets
]

FAILURES: list[str] = []
CHECKS: list = []


def fail(msg: str) -> None:
    FAILURES.append(msg)


def check(fn):
    CHECKS.append(fn)
    return fn


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text())


def front_matter(path: Path) -> tuple[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        fail(f"{path}: no YAML front matter")
        return "", text
    end = text.index("\n---\n", 3)
    return text[4:end], text[end + 5:]


def scalar(block: str, key: str) -> str:
    """Read a scalar or a folded (>-) block value. No YAML dependency by design."""
    m = re.search(rf"^{key}:\s*(.*)$", block, re.M)
    if not m:
        return ""
    value = m.group(1).strip()
    if value in (">-", ">", "|", "|-"):
        lines = []
        started = False
        for line in block[m.end():].splitlines():
            if not started and not line.strip():
                continue
            if line.startswith("  ") or not line.strip():
                started = True
                lines.append(line.strip())
            else:
                break
        return " ".join(x for x in lines if x)
    return value.strip("'\"")


def skills() -> list[Path]:
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


# --------------------------------------------------------------------- structure

@check
def check_every_skill_dir_ships_a_body():
    found = skills()
    if not found:
        fail("no skills found under plugins/xr-dev/skills")
    for s in found:
        if not (s / "SKILL.md").is_file():
            fail(f"{s.name}: no SKILL.md")


@check
def check_one_version_in_every_place():
    mk = load_json(".claude-plugin/marketplace.json")
    entry = next(p for p in mk["plugins"] if p["name"] == PLUGIN)
    versions = {
        "marketplace.json": entry["version"],
        "plugin.json": load_json(f"plugins/{PLUGIN}/.claude-plugin/plugin.json")["version"],
        "package.json": load_json("package.json")["version"],
    }
    changelog = (ROOT / "CHANGELOG.md").read_text()
    m = re.search(r"^##\s*\[?v?(\d+\.\d+\.\d+)\]?", changelog, re.M)
    versions["CHANGELOG.md"] = m.group(1) if m else "<none>"
    for s in skills():
        block, _ = front_matter(s / "SKILL.md")
        v = scalar(block, "  version") or re.search(r"version:\s*([0-9.]+)", block)
        versions[f"{s.name}/SKILL.md"] = v.group(1) if hasattr(v, "group") else (v or "<none>")
    if len(set(versions.values())) != 1:
        fail("version drift: " + ", ".join(f"{k}={v}" for k, v in sorted(versions.items())))


@check
def check_schema_addresses_are_pinned():
    mk = load_json(".claude-plugin/marketplace.json")
    pl = load_json(f"plugins/{PLUGIN}/.claude-plugin/plugin.json")
    if mk.get("$schema") != SCHEMAS["marketplace"]:
        fail(f"marketplace.json $schema is {mk.get('$schema')!r}, expected {SCHEMAS['marketplace']!r}")
    if pl.get("$schema") != SCHEMAS["plugin"]:
        fail(f"plugin.json $schema is {pl.get('$schema')!r}, expected {SCHEMAS['plugin']!r}")
    for name, doc in (("plugin.json", pl), ("marketplace entry", next(p for p in mk["plugins"] if p["name"] == PLUGIN))):
        for field in ("displayName", "license", "description", "version"):
            if not doc.get(field):
                fail(f"{name}: missing {field}")
    if "$schema" in mk["plugins"][0]:
        fail("marketplace ENTRY carries $schema; only the two manifest roots take it")


# ------------------------------------------------------------------ front matter

@check
def check_skill_front_matter():
    for s in skills():
        block, _ = front_matter(s / "SKILL.md")
        name = scalar(block, "name")
        desc = scalar(block, "description")
        if name != s.name:
            fail(f"{s.name}: front-matter name is {name!r}")
        if re.search(r"claude|anthropic", name, re.I):
            fail(f"{s.name}: name contains a reserved substring (claude/anthropic)")
        if not scalar(block, "license"):
            fail(f"{s.name}: no license in front matter")
        if len(desc) > DESC_CAP:
            fail(f"{s.name}: description {len(desc)} chars over the {DESC_CAP} cap")
        elif len(desc) > DESC_HOUSE:
            fail(f"{s.name}: description {len(desc)} chars over the house cap {DESC_HOUSE}")
        if not desc.startswith("Use when"):
            fail(f"{s.name}: description does not start with 'Use when'")
        if "<" in desc or ">" in desc:
            fail(f"{s.name}: description contains an angle bracket")
        if re.search(r"\b(I|we|you)\b (can|will|should) help", desc, re.I):
            fail(f"{s.name}: description is not third person")
        if not re.search(r"[А-Яа-яЁё]", desc):
            fail(f"{s.name}: description carries no Russian trigger phrase")
        if "NOT for" not in desc:
            fail(f"{s.name}: description states no boundary ('NOT for ...')")


@check
def check_body_budget():
    for s in skills():
        _, body = front_matter(s / "SKILL.md")
        lines = len(body.splitlines())
        tokens = int(len(body) / CHARS_PER_TOKEN)
        if lines > BODY_LINES_CAP:
            fail(f"{s.name}: body {lines} lines over the {BODY_LINES_CAP} cap")
        elif lines > BODY_LINES_HOUSE:
            fail(f"{s.name}: body {lines} lines over the house cap {BODY_LINES_HOUSE}")
        if tokens > BODY_TOKENS_CAP:
            fail(f"{s.name}: body ~{tokens} tokens over the {BODY_TOKENS_CAP} cap")
        elif tokens > BODY_TOKENS_HOUSE:
            fail(f"{s.name}: body ~{tokens} tokens over the house cap {BODY_TOKENS_HOUSE}")


# -------------------------------------------------------------------- references

@check
def check_references_resolve_both_ways():
    for s in skills():
        _, body = front_matter(s / "SKILL.md")
        named = set(re.findall(r"`references/([A-Za-z0-9._-]+)`", body))
        on_disk = {p.name for p in (s / "references").glob("*.md")} if (s / "references").is_dir() else set()
        for missing in sorted(named - on_disk):
            fail(f"{s.name}: body names references/{missing}, which does not ship")
        for orphan in sorted(on_disk - named):
            fail(f"{s.name}: references/{orphan} ships but no body names it")
        for ref in sorted(on_disk):
            text = (s / "references" / ref).read_text()
            if len(text.splitlines()) > 100 and "## Contents" not in text:
                fail(f"{s.name}/references/{ref}: over 100 lines without a '## Contents' section")
            if not re.search(r"\*\*Read this when\*\*", text):
                fail(f"{s.name}/references/{ref}: no '**Read this when**' load trigger")
        for deep in (s / "references").rglob("*/*") if (s / "references").is_dir() else []:
            fail(f"{s.name}: references nest more than one level deep ({deep})")


@check
def check_no_stray_skill_md():
    for p in ROOT.rglob("SKILL.md"):
        if ".git" in p.parts:
            continue
        if p.parent.parent != SKILLS_DIR:
            fail(f"stray SKILL.md outside the skill dirs: {p.relative_to(ROOT)} — it would ship as a real skill")


@check
def check_no_secret_shapes_in_the_payload():
    for p in list(PLUGIN_DIR.rglob("*.md")) + list(ROOT.glob("*.md")):
        text = p.read_text()
        for shape in SECRET_SHAPES:
            if shape.search(text):
                fail(f"{p.relative_to(ROOT)}: a credential-shaped string is in the payload")


# ------------------------------------------------------------------- the outside

@check
def check_the_readme_counts_what_ships():
    readme = (ROOT / "README.md").read_text()
    names = [s.name for s in skills()]
    for n in names:
        if n not in readme:
            fail(f"README.md does not mention the skill {n}")
    # The README must state the count SOMEWHERE and state it correctly. Scanning
    # every "<word> skills" and requiring one right answer beats pinning a single
    # phrasing: the first sentence of a README is prose, not a counter.
    words = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
    expected = {words.get(len(names)), str(len(names))} - {None}
    said = {m.lower() for m in re.findall(r"([A-Za-z]+|\d+) skills\b", readme)}
    if not (said & expected):
        fail(f"README never states the skill count correctly ({len(names)} ship; it says {sorted(said)})")


@check
def check_ci_runs_the_gate():
    ci = (ROOT / ".github/workflows/validate.yml").read_text()
    for needle in ("npm test", "npm run test:negatives",
                   "claude plugin validate . --strict",
                   f"claude plugin validate plugins/{PLUGIN} --strict"):
        if needle not in ci:
            fail(f"validate.yml does not run: {needle}")


@check
def check_links_resolve_and_stay_inside():
    for md in PLUGIN_DIR.rglob("*.md"):
        for target in re.findall(r"\]\((?!https?:|mailto:|#)([^)]+)\)", md.read_text()):
            dest = (md.parent / target.split("#")[0]).resolve()
            if not dest.exists():
                fail(f"{md.relative_to(ROOT)}: broken relative link -> {target}")
            elif PLUGIN_DIR.resolve() not in dest.parents and dest != PLUGIN_DIR.resolve():
                fail(f"{md.relative_to(ROOT)}: link escapes the plugin dir -> {target}")


# --------------------------------------------------------------------- self-test

DEFECTS = [
    ("version drift",
     lambda r: _patch_json(r / "package.json", {"version": "9.9.9"})),
    ("description over the house cap",
     lambda r: _patch_desc(r, "x" * 1000)),
    ("description without a Russian trigger",
     lambda r: _patch_desc(r, "Use when something happens. NOT for anything else.")),
    ("a reference that stopped shipping",
     lambda r: (r / "plugins/xr-dev/skills/quest-perf/references/capture-playbook.md").unlink()),
    ("a stray SKILL.md at the repo root",
     lambda r: (r / "SKILL.md").write_text("---\nname: stray\n---\n")),
    ("a credential-shaped string in the payload",
     lambda r: _append(r / "plugins/xr-dev/skills/quest-tooling/SKILL.md",
                       "\ntoken: sk-abcdefghijklmnopqrstuvwxyz012345\n")),
    ("the CI gate removed",
     lambda r: _rewrite(r / ".github/workflows/validate.yml", "npm test", "true")),
    ("a broken relative link",
     lambda r: _append(r / "plugins/xr-dev/skills/quest-native/SKILL.md",
                       "\nSee [gone](references/not-here.md).\n")),
]


def _patch_json(path: Path, patch: dict) -> None:
    doc = json.loads(path.read_text())
    doc.update(patch)
    path.write_text(json.dumps(doc, indent=2) + "\n")


def _patch_desc(root: Path, desc: str) -> None:
    p = root / "plugins/xr-dev/skills/quest-store/SKILL.md"
    text = p.read_text()
    start = text.index("description:")
    end = text.index("\nlicense:", start)
    p.write_text(text[:start] + f"description: {desc}" + text[end:])


def _append(path: Path, extra: str) -> None:
    path.write_text(path.read_text() + extra)


def _rewrite(path: Path, old: str, new: str) -> None:
    path.write_text(path.read_text().replace(old, new))


def self_test() -> int:
    bad = []
    for label, plant in DEFECTS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "node_modules"))
            plant(copy)
            rc = subprocess.run([sys.executable, str(copy / "test/validate.py")],
                                capture_output=True, text=True)
            if rc.returncode == 0:
                bad.append(label)
                print(f"NOT CAUGHT: {label}")
            else:
                first = next((l for l in rc.stdout.splitlines() if l.startswith("  - ")), "")
                print(f"caught: {label}{first and ' ->' + first[3:]}")
    print()
    if bad:
        print(f"SELF-TEST FAILED: {len(bad)} planted defect(s) went unnoticed")
        return 1
    print(f"SELF-TEST OK: all {len(DEFECTS)} planted defects were caught")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    for fn in CHECKS:
        fn()
    if FAILURES:
        print(f"FAIL — {len(FAILURES)} problem(s):")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"OK — {len(CHECKS)} checks, {len(skills())} skills, "
          f"{sum(1 for _ in PLUGIN_DIR.rglob('references/*.md'))} references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
