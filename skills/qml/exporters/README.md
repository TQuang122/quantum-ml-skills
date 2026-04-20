# QML Exporters

This directory contains export utilities that transform the local QML skill library into platform-specific skill package layouts.

The source-of-truth remains:

- `skills/qml/`

Exporters should read from the source library and write generated output into:

- `skills/qml/exports/<platform>/`

## Current exporters

- `export_opencode.py` — initial scaffold for exporting the QML skill library into an OpenCode-compatible structure
- `export_claude_code.py` — exports the QML skill library into a Claude Code-compatible structure
- `export_claude_marketplace.py` — exports the QML skill library into a local Claude Code marketplace with installable plugin bundles

## Current scope

The initial OpenCode exporter focuses on:

- validating source `SKILL.md` frontmatter at a basic level
- copying supported source files into an OpenCode skill layout
- preserving the source library without mutating it

## CLI support

The current `export_opencode.py` supports:

- export all skills into `skills/qml/exports/opencode/`
- export one skill with `--skill <name>`
- install all skills directly into a chosen OpenCode skills path with `--install-to <path>`
- install one skill with `--skill <name> --install-to <path>`
- JSON summary output after execution

The current `export_claude_code.py` supports:

- export all skills into `skills/qml/exports/claude-code/`
- export one skill with `--skill <name>`
- install all skills directly into a chosen Claude Code skills path with `--install-to <path>`
- install one skill with `--skill <name> --install-to <path>`
- JSON summary output after execution

The current `export_claude_marketplace.py` supports:

- export all plugin bundles into `skills/qml/exports/claude-marketplace/`
- export one plugin bundle with `--plugin <name>`
- install all plugin bundles directly into a chosen local Claude marketplace path with `--install-to <path>`
- install one plugin bundle with `--plugin <name> --install-to <path>`
- sync all plugin bundles into the repository root for GitHub-hosted marketplace use with `--sync-hosted-root`
- JSON summary output after execution

## Examples

OpenCode exporter:

```bash
python skills/qml/exporters/export_opencode.py
python skills/qml/exporters/export_opencode.py --skill qml-pytorch-training
python skills/qml/exporters/export_opencode.py --install-to .opencode/skills
python skills/qml/exporters/export_opencode.py --skill pennylane-qnn --install-to .opencode/skills
```

Claude Code exporter:

```bash
python skills/qml/exporters/export_claude_code.py
python skills/qml/exporters/export_claude_code.py --skill qml-pytorch-training
python skills/qml/exporters/export_claude_code.py --install-to .claude/skills
python skills/qml/exporters/export_claude_code.py --skill pennylane-qnn --install-to .claude/skills
```

Claude Code marketplace exporter:

```bash
python skills/qml/exporters/export_claude_marketplace.py
python skills/qml/exporters/export_claude_marketplace.py --plugin qml-core
python skills/qml/exporters/export_claude_marketplace.py --install-to .claude/marketplaces/qml-skills
python skills/qml/exporters/export_claude_marketplace.py --plugin qml-research --install-to .claude/marketplaces/qml-skills
python skills/qml/exporters/export_claude_marketplace.py --sync-hosted-root
```

It does **not** yet implement all possible platform-specific metadata remapping.
