# Contributing

## Goal

Contributions should improve the QML skill library while preserving:

- PennyLane-first architecture
- PyTorch-first training and interface flow
- exportability to OpenCode first, then other platforms later

## Contribution areas

Useful contributions include:

- new QML skills
- better request patterns and routing guidance
- stronger prompts and examples
- starter templates
- exporter improvements
- installer improvements

## Before opening a change

1. identify whether the change belongs in the source library or a platform export layer
2. avoid editing generated exports by hand when an exporter should own them
3. keep skill naming lowercase and hyphen-separated
4. preserve or update frontmatter metadata when modifying `SKILL.md`

## Skill changes

When editing a skill:

- update `SKILL.md`
- update `prompts/quickstart.md` if usage changes
- update `examples/workflows.md` if workflow expectations change
- keep `name` aligned with the folder name
- keep `depends_on` and `handoff_to` accurate

## Exporter changes

When editing an exporter:

- keep `skills/qml/` as the source-of-truth
- do not hard-code source-specific assumptions that block future Claude Code or Antigravity exporters
- prefer clear file mappings over platform-specific hacks

## Validation

Before considering a change complete:

- read back modified markdown docs
- run Python diagnostics on changed exporter/installer code when possible
- make sure generated output docs still match actual behavior

## Suggested workflow

1. update source files first
2. update exporter/installer logic second
3. regenerate output if needed
4. update docs last so usage instructions stay accurate
