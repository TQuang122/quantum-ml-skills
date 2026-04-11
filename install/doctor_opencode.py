from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "category",
    "maturity",
    "platforms",
    "depends_on",
    "handoff_to",
}
EXPECTED_SKILL_COUNT = 9


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate an OpenCode skills install directory for Quantum ML skills."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd() / ".opencode" / "skills",
        help="OpenCode skills directory to inspect. Defaults to ./.opencode/skills/.",
    )
    return parser


def list_skill_dirs(root: Path) -> list[Path]:
    if not root.exists() or not root.is_dir():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir())


def split_frontmatter(text: str) -> tuple[list[str], str] | None:
    if not text.startswith("---\n"):
        return None

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return None

    raw_frontmatter = parts[0].splitlines()[1:]
    body = parts[1]
    return raw_frontmatter, body


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


def validate_frontmatter(skill_dir: Path) -> dict[str, object]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {
            "has_frontmatter": False,
            "frontmatter_valid": False,
            "missing_frontmatter_keys": sorted(REQUIRED_FRONTMATTER_KEYS),
            "frontmatter_name_matches_dir": False,
            "platforms_include_opencode": False,
        }

    text = skill_md.read_text(encoding="utf-8")
    split_result = split_frontmatter(text)
    if split_result is None:
        return {
            "has_frontmatter": False,
            "frontmatter_valid": False,
            "missing_frontmatter_keys": sorted(REQUIRED_FRONTMATTER_KEYS),
            "frontmatter_name_matches_dir": False,
            "platforms_include_opencode": False,
        }

    raw_frontmatter, _ = split_result

    try:
        frontmatter = parse_simple_yaml(raw_frontmatter)
    except ValueError:
        return {
            "has_frontmatter": True,
            "frontmatter_valid": False,
            "missing_frontmatter_keys": sorted(REQUIRED_FRONTMATTER_KEYS),
            "frontmatter_name_matches_dir": False,
            "platforms_include_opencode": False,
        }

    missing_keys = sorted(REQUIRED_FRONTMATTER_KEYS - set(frontmatter))
    name_matches = frontmatter.get("name") == skill_dir.name
    platforms = frontmatter.get("platforms", [])
    platforms_include_opencode = isinstance(platforms, list) and "opencode" in platforms

    return {
        "has_frontmatter": True,
        "frontmatter_valid": len(missing_keys) == 0,
        "missing_frontmatter_keys": missing_keys,
        "frontmatter_name_matches_dir": name_matches,
        "platforms_include_opencode": platforms_include_opencode,
    }


def check_skill(skill_dir: Path) -> dict[str, object]:
    skill_md = skill_dir / "SKILL.md"
    prompt_ref = skill_dir / "references" / "prompts" / "quickstart.md"
    example_ref = skill_dir / "references" / "examples" / "workflows.md"
    frontmatter_report = validate_frontmatter(skill_dir)

    return {
        "name": skill_dir.name,
        "has_skill_md": skill_md.exists(),
        "has_prompt_reference": prompt_ref.exists(),
        "has_example_reference": example_ref.exists(),
        **frontmatter_report,
    }


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    root = args.path.resolve()
    skill_dirs = list_skill_dirs(root)
    results = [check_skill(skill_dir) for skill_dir in skill_dirs]
    root_name = root.name
    expected_namespaced_root = root_name == "qml-skills"
    all_frontmatter_valid = all(result["frontmatter_valid"] for result in results)
    all_name_matches = all(result["frontmatter_name_matches_dir"] for result in results)
    all_include_opencode = all(
        result["platforms_include_opencode"] for result in results
    )

    print(
        json.dumps(
            {
                "checked_path": str(root),
                "skill_count": len(results),
                "expected_skill_count": EXPECTED_SKILL_COUNT,
                "expected_skill_count_met": len(results) == EXPECTED_SKILL_COUNT,
                "namespaced_root": expected_namespaced_root,
                "all_frontmatter_valid": all_frontmatter_valid,
                "all_frontmatter_names_match": all_name_matches,
                "all_platforms_include_opencode": all_include_opencode,
                "skills": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
