from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT
EXPORT_ROOT = ROOT / "exports" / "opencode"


@dataclass(slots=True)
class SkillPaths:
    source_dir: Path
    target_dir: Path
    skill_md: Path


@dataclass(slots=True)
class ExportRecord:
    name: str
    source_dir: str
    target_dir: str


@dataclass(slots=True)
class ExportSummary:
    mode: str
    source_root: str
    output_root: str
    selected_skill: str | None
    dry_run: bool
    exported: list[ExportRecord]
    skipped: list[str]


def list_skill_dirs(skills_root: Path) -> list[Path]:
    skill_dirs: list[Path] = []
    for path in sorted(skills_root.iterdir()):
        if not path.is_dir():
            continue
        if path.name in {"templates", "exports", "exporters"}:
            continue
        skill_md = path / "SKILL.md"
        if skill_md.exists():
            skill_dirs.append(path)
    return skill_dirs


def find_skill_dir(skills_root: Path, skill_name: str) -> Path:
    skill_dir = skills_root / skill_name
    skill_md = skill_dir / "SKILL.md"
    if not skill_dir.is_dir() or not skill_md.exists():
        raise ValueError(f"Unknown skill '{skill_name}' in {skills_root}")
    return skill_dir


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter")

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("Invalid frontmatter block")

    raw_frontmatter = parts[0].splitlines()[1:]
    body = parts[1]
    frontmatter = parse_simple_yaml(raw_frontmatter)
    return frontmatter, body


def parse_simple_yaml(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
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


def validate_frontmatter(frontmatter: dict[str, Any], folder_name: str) -> None:
    required_keys = {"name", "description", "platforms"}
    missing = sorted(required_keys - set(frontmatter))
    if missing:
        raise ValueError(f"Missing required frontmatter keys: {', '.join(missing)}")

    name = frontmatter["name"]
    if not isinstance(name, str) or name != folder_name:
        raise ValueError(
            f"Frontmatter name '{name}' must match folder name '{folder_name}'"
        )

    description = frontmatter["description"]
    if not isinstance(description, str) or not description.strip():
        raise ValueError("description must be a non-empty string")

    platforms = frontmatter["platforms"]
    if not isinstance(platforms, list):
        raise ValueError("platforms must be a list")


def should_export_to_opencode(frontmatter: dict[str, Any]) -> bool:
    platforms = frontmatter.get("platforms", [])
    return isinstance(platforms, list) and "opencode" in platforms


def map_skill(source_dir: Path, export_root: Path) -> SkillPaths:
    target_dir = export_root / source_dir.name
    return SkillPaths(
        source_dir=source_dir, target_dir=target_dir, skill_md=source_dir / "SKILL.md"
    )


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_if_exists(source: Path, target: Path) -> None:
    if source.exists():
        if source.is_dir():
            shutil.copytree(source, target, dirs_exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


def copy_if_exists_dry_run(source: Path, target: Path, dry_run: bool) -> None:
    if dry_run:
        return
    copy_if_exists(source, target)


def export_skill(skill: SkillPaths, dry_run: bool) -> None:
    if not dry_run:
        skill.target_dir.mkdir(parents=True, exist_ok=True)
    copy_if_exists_dry_run(skill.skill_md, skill.target_dir / "SKILL.md", dry_run)
    copy_if_exists_dry_run(
        skill.source_dir / "prompts",
        skill.target_dir / "references" / "prompts",
        dry_run,
    )
    copy_if_exists_dry_run(
        skill.source_dir / "examples",
        skill.target_dir / "references" / "examples",
        dry_run,
    )


def export_selected(
    skill_dirs: list[Path],
    export_root: Path,
    reset_output: bool,
    selected_skill: str | None,
    mode: str,
    dry_run: bool,
) -> ExportSummary:
    exported: list[ExportRecord] = []
    skipped: list[str] = []

    if not dry_run:
        if reset_output:
            reset_directory(export_root)
        else:
            export_root.mkdir(parents=True, exist_ok=True)

    for skill_dir in skill_dirs:
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        frontmatter, _ = split_frontmatter(text)
        validate_frontmatter(frontmatter, skill_dir.name)

        if not should_export_to_opencode(frontmatter):
            skipped.append(skill_dir.name)
            continue

        skill = map_skill(skill_dir, export_root)
        export_skill(skill, dry_run)
        exported.append(
            ExportRecord(
                name=skill_dir.name,
                source_dir=str(skill.source_dir),
                target_dir=str(skill.target_dir),
            )
        )

    return ExportSummary(
        mode=mode,
        source_root=str(SKILLS_ROOT),
        output_root=str(export_root),
        selected_skill=selected_skill,
        dry_run=dry_run,
        exported=exported,
        skipped=skipped,
    )


def export_all(skills_root: Path, export_root: Path, dry_run: bool) -> ExportSummary:
    return export_selected(
        skill_dirs=list_skill_dirs(skills_root),
        export_root=export_root,
        reset_output=True,
        selected_skill=None,
        mode="export-all",
        dry_run=dry_run,
    )


def export_one(
    skills_root: Path, export_root: Path, skill_name: str, dry_run: bool
) -> ExportSummary:
    return export_selected(
        skill_dirs=[find_skill_dir(skills_root, skill_name)],
        export_root=export_root,
        reset_output=False,
        selected_skill=skill_name,
        mode="export-one",
        dry_run=dry_run,
    )


def install_all(skills_root: Path, install_root: Path, dry_run: bool) -> ExportSummary:
    return export_selected(
        skill_dirs=list_skill_dirs(skills_root),
        export_root=install_root,
        reset_output=False,
        selected_skill=None,
        mode="install-all",
        dry_run=dry_run,
    )


def install_one(
    skills_root: Path, install_root: Path, skill_name: str, dry_run: bool
) -> ExportSummary:
    return export_selected(
        skill_dirs=[find_skill_dir(skills_root, skill_name)],
        export_root=install_root,
        reset_output=False,
        selected_skill=skill_name,
        mode="install-one",
        dry_run=dry_run,
    )


def print_summary(summary: ExportSummary) -> None:
    print(
        json.dumps(
            {
                "mode": summary.mode,
                "source_root": summary.source_root,
                "output_root": summary.output_root,
                "selected_skill": summary.selected_skill,
                "dry_run": summary.dry_run,
                "exported_count": len(summary.exported),
                "skipped_count": len(summary.skipped),
                "exported": [
                    {
                        "name": item.name,
                        "source_dir": item.source_dir,
                        "target_dir": item.target_dir,
                    }
                    for item in summary.exported
                ],
                "skipped": summary.skipped,
            },
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Export local QML skills to an OpenCode-compatible layout."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=SKILLS_ROOT,
        help="Source skills root. Defaults to skills/qml/.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=EXPORT_ROOT,
        help="OpenCode export output directory. Defaults to skills/qml/exports/opencode/.",
    )
    parser.add_argument(
        "--skill",
        type=str,
        default=None,
        help="Export or install a single skill by name instead of all skills.",
    )
    parser.add_argument(
        "--install-to",
        type=Path,
        default=None,
        help="Install directly into a target OpenCode skills directory, such as .opencode/skills/.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and report actions without writing output.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.install_to is not None:
        target_root = args.install_to
        if args.skill is not None:
            summary = install_one(args.source, target_root, args.skill, args.dry_run)
        else:
            summary = install_all(args.source, target_root, args.dry_run)
    else:
        target_root = args.output
        if args.skill is not None:
            summary = export_one(args.source, target_root, args.skill, args.dry_run)
        else:
            summary = export_all(args.source, target_root, args.dry_run)

    print_summary(summary)


if __name__ == "__main__":
    main()
