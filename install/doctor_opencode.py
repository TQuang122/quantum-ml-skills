from __future__ import annotations

import argparse
import json
from pathlib import Path


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


def check_skill(skill_dir: Path) -> dict[str, object]:
    skill_md = skill_dir / "SKILL.md"
    prompt_ref = skill_dir / "references" / "prompts" / "quickstart.md"
    example_ref = skill_dir / "references" / "examples" / "workflows.md"

    return {
        "name": skill_dir.name,
        "has_skill_md": skill_md.exists(),
        "has_prompt_reference": prompt_ref.exists(),
        "has_example_reference": example_ref.exists(),
    }


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    root = args.path.resolve()
    skill_dirs = list_skill_dirs(root)
    results = [check_skill(skill_dir) for skill_dir in skill_dirs]

    print(
        json.dumps(
            {
                "checked_path": str(root),
                "skill_count": len(results),
                "skills": results,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
