from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, cast


EXPECTED_PLUGIN_NAMES = {
    "qml-common",
    "qml-core",
    "qml-backends",
    "qml-evaluation",
    "qml-research",
}
EXPECTED_SKILL_COUNT = 12
REQUIRED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "category",
    "maturity",
    "platforms",
    "depends_on",
    "handoff_to",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a local Claude Code marketplace install for Quantum ML skills."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd() / ".claude" / "marketplaces" / "qml-skills",
        help="Claude marketplace directory to inspect. Defaults to ./.claude/marketplaces/qml-skills/.",
    )
    return parser


def split_frontmatter(text: str) -> tuple[list[str], str] | None:
    if not text.startswith("---\n"):
        return None

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return None

    return parts[0].splitlines()[1:], parts[1]


def parse_simple_yaml(lines: list[str]) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line:
            continue

        if line.startswith("  - "):
            if current_key is None:
                raise ValueError("List item without active key")
            current_value = data.setdefault(current_key, [])
            if not isinstance(current_value, list):
                raise ValueError(f"Key '{current_key}' is not a list")
            current_value.append(line[4:].strip())
            continue

        if ":" not in line:
            raise ValueError(f"Unsupported YAML line: {line}")

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value == "[]":
            data[key] = []
        elif value == "":
            data[key] = []
        else:
            data[key] = value
        current_key = key

    return data


def validate_skill(skill_dir: Path) -> dict[str, object]:
    skill_md = skill_dir / "SKILL.md"
    prompt_ref = skill_dir / "references" / "prompts" / "quickstart.md"
    example_ref = skill_dir / "references" / "examples" / "workflows.md"
    if not skill_md.exists():
        return {
            "name": skill_dir.name,
            "has_skill_md": False,
            "has_prompt_reference": prompt_ref.exists(),
            "has_example_reference": example_ref.exists(),
            "has_frontmatter": False,
            "frontmatter_valid": False,
            "missing_frontmatter_keys": sorted(REQUIRED_FRONTMATTER_KEYS),
            "frontmatter_name_matches_dir": False,
            "platforms_include_claude_code": False,
        }

    text = skill_md.read_text(encoding="utf-8")
    split_result = split_frontmatter(text)
    if split_result is None:
        return {
            "name": skill_dir.name,
            "has_skill_md": True,
            "has_prompt_reference": prompt_ref.exists(),
            "has_example_reference": example_ref.exists(),
            "has_frontmatter": False,
            "frontmatter_valid": False,
            "missing_frontmatter_keys": sorted(REQUIRED_FRONTMATTER_KEYS),
            "frontmatter_name_matches_dir": False,
            "platforms_include_claude_code": False,
        }

    raw_frontmatter, _ = split_result
    try:
        frontmatter = parse_simple_yaml(raw_frontmatter)
    except ValueError:
        return {
            "name": skill_dir.name,
            "has_skill_md": True,
            "has_prompt_reference": prompt_ref.exists(),
            "has_example_reference": example_ref.exists(),
            "has_frontmatter": True,
            "frontmatter_valid": False,
            "missing_frontmatter_keys": sorted(REQUIRED_FRONTMATTER_KEYS),
            "frontmatter_name_matches_dir": False,
            "platforms_include_claude_code": False,
        }

    missing_keys = sorted(REQUIRED_FRONTMATTER_KEYS - set(frontmatter))
    name_matches = frontmatter.get("name") == skill_dir.name
    platforms = frontmatter.get("platforms", [])
    platforms_include_claude_code = (
        isinstance(platforms, list) and "claude-code" in platforms
    )

    return {
        "name": skill_dir.name,
        "has_skill_md": True,
        "has_prompt_reference": prompt_ref.exists(),
        "has_example_reference": example_ref.exists(),
        "has_frontmatter": True,
        "frontmatter_valid": len(missing_keys) == 0,
        "missing_frontmatter_keys": missing_keys,
        "frontmatter_name_matches_dir": name_matches,
        "platforms_include_claude_code": platforms_include_claude_code,
    }


def inspect_plugin(plugin_dir: Path) -> dict[str, object]:
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    skills_root = plugin_dir / "skills"
    skill_dirs = (
        sorted(path for path in skills_root.iterdir() if path.is_dir())
        if skills_root.exists()
        else []
    )
    skills = [validate_skill(skill_dir) for skill_dir in skill_dirs]
    return {
        "name": plugin_dir.name,
        "has_plugin_manifest": manifest_path.exists(),
        "skill_count": len(skills),
        "skills": skills,
    }


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    root = args.path.resolve()
    marketplace_manifest = root / ".claude-plugin" / "marketplace.json"
    plugins_root = root / "plugins"
    plugin_dirs = (
        sorted(path for path in plugins_root.iterdir() if path.is_dir())
        if plugins_root.exists()
        else []
    )
    plugin_reports = [inspect_plugin(plugin_dir) for plugin_dir in plugin_dirs]
    skill_count = sum(cast(int, report["skill_count"]) for report in plugin_reports)
    plugin_names = {report["name"] for report in plugin_reports}
    all_plugin_manifests = all(
        report["has_plugin_manifest"] for report in plugin_reports
    )
    all_skills_valid = all(
        cast(dict[str, Any], skill)["frontmatter_valid"]
        and cast(dict[str, Any], skill)["frontmatter_name_matches_dir"]
        and cast(dict[str, Any], skill)["platforms_include_claude_code"]
        for report in plugin_reports
        for skill in cast(list[dict[str, Any]], report["skills"])
    )

    print(
        json.dumps(
            {
                "checked_path": str(root),
                "has_marketplace_manifest": marketplace_manifest.exists(),
                "plugin_count": len(plugin_reports),
                "expected_plugin_count": len(EXPECTED_PLUGIN_NAMES),
                "expected_plugin_count_met": len(plugin_reports)
                == len(EXPECTED_PLUGIN_NAMES),
                "plugin_names_match": plugin_names == EXPECTED_PLUGIN_NAMES,
                "all_plugin_manifests": all_plugin_manifests,
                "skill_count": skill_count,
                "expected_skill_count": EXPECTED_SKILL_COUNT,
                "expected_skill_count_met": skill_count == EXPECTED_SKILL_COUNT,
                "all_skills_valid": all_skills_valid,
                "plugins": plugin_reports,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
