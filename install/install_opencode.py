from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "skills" / "qml" / "exporters" / "export_opencode.py"


@dataclass(slots=True)
class InstallConfig:
    target_dir: Path
    skill: str | None
    dry_run: bool


def default_global_target() -> Path:
    return Path.home() / ".config" / "opencode" / "skills" / "qml-skills"


def project_target(project_root: Path) -> Path:
    return project_root / ".opencode" / "skills"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install Quantum ML skills into an OpenCode skills directory."
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Project root where .opencode/skills/ should be created.",
    )
    parser.add_argument(
        "--global",
        dest="use_global",
        action="store_true",
        help="Install into the global OpenCode config at ~/.config/opencode/skills/.",
    )
    parser.add_argument(
        "--skill",
        type=str,
        default=None,
        help="Install only one skill by name.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and report installation actions without writing files.",
    )
    return parser


def resolve_config(args: argparse.Namespace) -> InstallConfig:
    if args.use_global and args.project_root is not None:
        raise ValueError("Use either --global or --project-root, not both")

    if args.use_global:
        target_dir = default_global_target()
    else:
        project_root = args.project_root or Path.cwd()
        target_dir = project_target(project_root.resolve())

    return InstallConfig(target_dir=target_dir, skill=args.skill, dry_run=args.dry_run)


def run_exporter(config: InstallConfig) -> int:
    command = [
        sys.executable,
        str(EXPORTER),
        "--install-to",
        str(config.target_dir),
    ]

    if config.skill is not None:
        command.extend(["--skill", config.skill])

    if config.dry_run:
        command.append("--dry-run")

    completed = subprocess.run(command, check=False)
    return completed.returncode


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        config = resolve_config(args)
    except ValueError as error:
        parser.error(str(error))
        return

    exit_code = run_exporter(config)
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
