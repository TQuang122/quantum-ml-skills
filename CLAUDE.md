# CLAUDE.md

This repository contains a reusable quantum machine learning skill library with a PennyLane-first design, PyTorch-first training flow, and exporter-based compatibility for multiple agent systems.

## Repository purpose

- maintain QML skills in one canonical source library
- support OpenCode today without blocking Claude Code usage
- preserve exportability to other platforms through an export layer instead of parallel hand-maintained copies

## Source of truth

The canonical source lives in:

- `skills/qml/`

Do not treat generated exports as editable source.

## Important paths

- `skills/qml/README.md` — skill library overview and structure
- `skills/qml/REQUEST_PATTERNS.md` — quick mapping from request shape to skill
- `skills/qml/ROUTING.md` — routing guidance when multiple skills overlap
- `skills/qml/EXPORT_STRATEGY.md` — source-first export model and platform mapping rules
- `skills/qml/exporters/` — exporter scripts for platform-specific outputs
- `skills/qml/exports/` — generated platform outputs

## How to work in this repo

1. Update source files in `skills/qml/` first.
2. Update exporter or installer logic second.
3. Regenerate exports if needed.
4. Update user-facing docs last.

## Contributor rules

- keep `skills/qml/` as the source-of-truth
- do not edit generated exports by hand when an exporter should own them
- keep `SKILL.md` frontmatter aligned with the folder name and platform metadata
- preserve OpenCode support while adding Claude Code compatibility
- prefer small, explicit exporter mappings over platform-specific hacks

## Claude Code usage guidance

Claude Code users should navigate the source library first:

- start at `skills/qml/README.md`
- use `skills/qml/REQUEST_PATTERNS.md` for quick matching
- use `skills/qml/ROUTING.md` when the correct skill is ambiguous
- use exported Claude-compatible output only as a generated distribution layer

## Platform compatibility

- OpenCode remains supported through `.opencode/` tooling and the OpenCode installer/exporter
- Claude Code compatibility is added through this root `CLAUDE.md`, project-level `.claude/` config, and exporter-generated output under `skills/qml/exports/claude-code/`

If a platform-specific behavior is needed, implement it in the export layer instead of forking the source library.
