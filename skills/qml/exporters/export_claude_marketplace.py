from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT
EXPORT_ROOT = ROOT / "exports" / "claude-marketplace"
MARKETPLACE_NAME = "qml-skills"
MARKETPLACE_VERSION = "0.1.1"


@dataclass(slots=True)
class PluginBundle:
    name: str
    description: str
    skills: tuple[str, ...]


PLUGIN_BUNDLES = (
    PluginBundle(
        name="qml-common",
        description="Shared QML foundations and routing skills for Claude Code.",
        skills=("qml-foundations", "qml-pytorch-router"),
    ),
    PluginBundle(
        name="qml-core",
        description="Core PennyLane and PyTorch implementation skills for Claude Code.",
        skills=(
            "pennylane-qnn",
            "qml-pytorch-interface",
            "qml-pytorch-training",
            "qml-pytorch-performance-patterns",
        ),
    ),
    PluginBundle(
        name="qml-backends",
        description="Backend and Qiskit interop skills for Claude Code.",
        skills=("pennylane-qiskit-backends", "qiskit-machine-learning-interop"),
    ),
    PluginBundle(
        name="qml-evaluation",
        description="Benchmarking and reproducibility skills for Claude Code.",
        skills=("qml-cross-framework-benchmarking", "qml-reproducibility"),
    ),
    PluginBundle(
        name="qml-research",
        description="Research debugging and paper replication skills for Claude Code.",
        skills=("qml-debugging", "qml-paper-replication"),
    ),
)


@dataclass(slots=True)
class ExportedSkill:
    plugin: str
    skill: str
    source_dir: str
    target_dir: str


@dataclass(slots=True)
class ExportSummary:
    mode: str
    source_root: str
    output_root: str
    selected_plugin: str | None
    dry_run: bool
    exported_plugins: list[str]
    exported_skills: list[ExportedSkill]


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


def should_export_to_claude_code(frontmatter: dict[str, Any]) -> bool:
    platforms = frontmatter.get("platforms", [])
    return isinstance(platforms, list) and "claude-code" in platforms


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


def write_json(path: Path, payload: dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def plugin_root(export_root: Path, plugin_name: str) -> Path:
    return export_root / "plugins" / plugin_name


def validate_bundle(bundle: PluginBundle, skills_root: Path) -> list[Path]:
    resolved: list[Path] = []
    for skill_name in bundle.skills:
        skill_dir = find_skill_dir(skills_root, skill_name)
        text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        frontmatter, _ = split_frontmatter(text)
        validate_frontmatter(frontmatter, skill_dir.name)
        if not should_export_to_claude_code(frontmatter):
            raise ValueError(
                f"Skill '{skill_name}' does not declare Claude Code support in platforms"
            )
        resolved.append(skill_dir)
    return resolved


def export_bundle(
    bundle: PluginBundle, skills_root: Path, export_root: Path, dry_run: bool
) -> list[ExportedSkill]:
    resolved_skills = validate_bundle(bundle, skills_root)
    root = plugin_root(export_root, bundle.name)

    write_json(
        root / ".claude-plugin" / "plugin.json",
        {
            "name": bundle.name,
            "description": bundle.description,
            "version": MARKETPLACE_VERSION,
            "author": {"name": "Quantum ML Skills"},
        },
        dry_run,
    )

    exported: list[ExportedSkill] = []
    for skill_dir in resolved_skills:
        target_skill_dir = root / "skills" / skill_dir.name
        copy_if_exists_dry_run(
            skill_dir / "SKILL.md", target_skill_dir / "SKILL.md", dry_run
        )
        copy_if_exists_dry_run(
            skill_dir / "prompts",
            target_skill_dir / "references" / "prompts",
            dry_run,
        )
        copy_if_exists_dry_run(
            skill_dir / "examples",
            target_skill_dir / "references" / "examples",
            dry_run,
        )
        exported.append(
            ExportedSkill(
                plugin=bundle.name,
                skill=skill_dir.name,
                source_dir=str(skill_dir),
                target_dir=str(target_skill_dir),
            )
        )
    return exported


def write_marketplace_manifest(
    export_root: Path, bundles: list[PluginBundle], dry_run: bool
) -> None:
    payload = {
        "name": MARKETPLACE_NAME,
        "owner": {"name": "Quantum ML Skills"},
        "plugins": [
            {
                "name": bundle.name,
                "source": f"./plugins/{bundle.name}",
                "description": bundle.description,
                "version": MARKETPLACE_VERSION,
            }
            for bundle in bundles
        ],
    }
    write_json(export_root / ".claude-plugin" / "marketplace.json", payload, dry_run)


def find_bundle(plugin_name: str) -> PluginBundle:
    for bundle in PLUGIN_BUNDLES:
        if bundle.name == plugin_name:
            return bundle
    raise ValueError(f"Unknown plugin bundle '{plugin_name}'")


def export_selected(
    bundles: list[PluginBundle],
    skills_root: Path,
    export_root: Path,
    reset_output: bool,
    selected_plugin: str | None,
    mode: str,
    dry_run: bool,
) -> ExportSummary:
    if not dry_run:
        if reset_output:
            reset_directory(export_root)
        else:
            export_root.mkdir(parents=True, exist_ok=True)

    write_marketplace_manifest(export_root, bundles, dry_run)

    exported_skills: list[ExportedSkill] = []
    for bundle in bundles:
        exported_skills.extend(export_bundle(bundle, skills_root, export_root, dry_run))

    return ExportSummary(
        mode=mode,
        source_root=str(skills_root),
        output_root=str(export_root),
        selected_plugin=selected_plugin,
        dry_run=dry_run,
        exported_plugins=[bundle.name for bundle in bundles],
        exported_skills=exported_skills,
    )


def export_all(skills_root: Path, export_root: Path, dry_run: bool) -> ExportSummary:
    return export_selected(
        bundles=list(PLUGIN_BUNDLES),
        skills_root=skills_root,
        export_root=export_root,
        reset_output=True,
        selected_plugin=None,
        mode="export-all",
        dry_run=dry_run,
    )


def export_one(
    skills_root: Path, export_root: Path, plugin_name: str, dry_run: bool
) -> ExportSummary:
    bundle = find_bundle(plugin_name)
    return export_selected(
        bundles=[bundle],
        skills_root=skills_root,
        export_root=export_root,
        reset_output=False,
        selected_plugin=plugin_name,
        mode="export-one",
        dry_run=dry_run,
    )


def install_all(skills_root: Path, install_root: Path, dry_run: bool) -> ExportSummary:
    return export_selected(
        bundles=list(PLUGIN_BUNDLES),
        skills_root=skills_root,
        export_root=install_root,
        reset_output=True,
        selected_plugin=None,
        mode="install-all",
        dry_run=dry_run,
    )


def install_one(
    skills_root: Path, install_root: Path, plugin_name: str, dry_run: bool
) -> ExportSummary:
    bundle = find_bundle(plugin_name)
    return export_selected(
        bundles=[bundle],
        skills_root=skills_root,
        export_root=install_root,
        reset_output=False,
        selected_plugin=plugin_name,
        mode="install-one",
        dry_run=dry_run,
    )


def print_summary(summary: ExportSummary) -> None:
    print(
        json.dumps(
            {
                "marketplace": MARKETPLACE_NAME,
                "mode": summary.mode,
                "source_root": summary.source_root,
                "output_root": summary.output_root,
                "selected_plugin": summary.selected_plugin,
                "dry_run": summary.dry_run,
                "exported_plugin_count": len(summary.exported_plugins),
                "exported_skill_count": len(summary.exported_skills),
                "exported_plugins": summary.exported_plugins,
                "exported_skills": [
                    {
                        "plugin": item.plugin,
                        "skill": item.skill,
                        "source_dir": item.source_dir,
                        "target_dir": item.target_dir,
                    }
                    for item in summary.exported_skills
                ],
            },
            indent=2,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Export local QML skills to a Claude Code local marketplace layout."
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
        help="Claude marketplace output directory. Defaults to skills/qml/exports/claude-marketplace/.",
    )
    parser.add_argument(
        "--plugin",
        type=str,
        default=None,
        help="Export or install a single plugin bundle by name instead of all bundles.",
    )
    parser.add_argument(
        "--install-to",
        type=Path,
        default=None,
        help="Install directly into a target Claude Code marketplace directory.",
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
        if args.plugin is not None:
            summary = install_one(args.source, target_root, args.plugin, args.dry_run)
        else:
            summary = install_all(args.source, target_root, args.dry_run)
    else:
        target_root = args.output
        if args.plugin is not None:
            summary = export_one(args.source, target_root, args.plugin, args.dry_run)
        else:
            summary = export_all(args.source, target_root, args.dry_run)

    print_summary(summary)


if __name__ == "__main__":
    main()
