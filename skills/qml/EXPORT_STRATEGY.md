# QML Skill Export Strategy

This document defines how the local QML skill library should be treated as a **source-of-truth** and later exported into platform-specific skill systems such as OpenCode, Claude Code, and Antigravity.

## Source of truth

The canonical source format is:

- `skills/qml/`

Everything in this directory should be maintained first here. Platform-specific packages should be derived from this source instead of edited independently.

## Why a source-first strategy

The QML library already contains richer structure than a minimal platform skill package:

- `SKILL.md`
- `prompts/quickstart.md`
- `examples/workflows.md`
- routing/navigation docs
- starter code templates

That makes the local library valuable beyond any single platform. Exporting from one source avoids duplication and drift.

## Normalized metadata model

Each `SKILL.md` should begin with YAML frontmatter using a cross-platform-safe schema.

### Required source fields

```yaml
---
name: qml-pytorch-training
description: Standardized training-loop skill for PennyLane + PyTorch.
category: training
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-pytorch-interface
handoff_to:
  - qml-cross-framework-benchmarking
---
```

### Field meanings

- `name` — canonical skill identifier; must match folder name
- `description` — short discovery text for platform indexing and human selection
- `category` — local/source metadata for grouping and export filtering
- `maturity` — one of `stable`, `experimental`, or `core`
- `platforms` — platforms the skill is intended to target
- `depends_on` — earlier skills or prerequisites
- `handoff_to` — likely follow-up skills after this one completes

## Naming rules

- lowercase only
- hyphen-separated words
- no spaces
- should match the folder name exactly

The current QML skill names already follow this rule.

## Platform mapping strategy

## OpenCode

### Target assumption

OpenCode can consume `SKILL.md`-based skill packages and may prefer project-local or user-level install paths such as:

- `.opencode/skills/<skill-name>/SKILL.md`

### Export approach

- preserve `SKILL.md`
- keep `name` and `description` directly in frontmatter
- map richer local docs into optional supporting files as needed
- derive any platform-specific fields later rather than storing them in the source library now

### Current fit

OpenCode is the best first export target because this workspace already contains `.opencode/` tooling.

## Claude Code

### Target assumption

Claude Code supports both standalone skills and plugin-based distribution. For this repository, the preferred local packaging layer is a generated local marketplace built from the same source library.

### Export approach

- keep the same normalized frontmatter
- export into Claude-compatible skill directories later
- support a local marketplace layout for namespaced Claude plugin bundles
- add Claude-specific metadata only in the export layer if required

### Local marketplace packaging

The minimal local plugin-style packaging model for this repo is:

- keep `skills/qml/` as the canonical source
- generate a local marketplace under `skills/qml/exports/claude-marketplace/`
- generate plugin manifests under `.claude-plugin/plugin.json`
- generate a marketplace catalog under `.claude-plugin/marketplace.json`
- group skills into a small number of installable plugin bundles rather than one plugin per skill

Recommended plugin bundles:

- `qml-common` → `qml-foundations`, `qml-pytorch-router`
- `qml-core` → `pennylane-qnn`, `qml-pytorch-interface`, `qml-pytorch-training`, `qml-pytorch-performance-patterns`
- `qml-backends` → `pennylane-qiskit-backends`, `qiskit-machine-learning-interop`
- `qml-evaluation` → `qml-cross-framework-benchmarking`, `qml-reproducibility`
- `qml-research` → `qml-debugging`, `qml-paper-replication`

This preserves a source-first model while creating a local install experience that feels close to marketplace usage inside Claude Code.

### GitHub-hosted marketplace packaging

For `owner/repo` marketplace add flows, Claude Code expects the marketplace root at the repository root. In this repo, that means syncing generated marketplace artifacts into:

- `.claude-plugin/marketplace.json`
- `plugins/`

The source of truth still remains in `skills/qml/`, and the hosted root view must be generated, not edited by hand.

Recommended hosted sync command:

```bash
python skills/qml/exporters/export_claude_marketplace.py --sync-hosted-root
```

This command should be re-run whenever the Claude marketplace export changes.

## Antigravity

### Target assumption

Antigravity also appears compatible with the same general skill format, with possible differences in discovery path or optional metadata.

### Export approach

- keep the same normalized frontmatter
- export into Antigravity-compatible directories later
- preserve local source metadata and translate only what is required at export time

## Recommended export directory layout

When implementation starts, use a generated-output structure like:

```text
skills/qml/
  exporters/
    export_opencode.py
    export_claude_code.py
    export_claude_marketplace.py
    export_antigravity.py
  exports/
    opencode/
    claude-code/
    claude-marketplace/
    antigravity/
  .claude-plugin/
  plugins/
```

The current step does **not** implement exporters yet. It only prepares the source library to support them.

## Current implementation status

The first exporter scaffold now exists for OpenCode:

- `exporters/export_opencode.py`
- generated output root: `exports/opencode/`

This scaffold currently:

- reads source skills from `skills/qml/`
- validates basic frontmatter fields
- exports `SKILL.md`
- maps `prompts/` and `examples/` into `references/` in the OpenCode output

It is intentionally minimal and can be extended later with platform-specific metadata translation.

The current scaffold now also supports:

- exporting all skills
- exporting one selected skill
- installing directly into a target OpenCode skills directory
- JSON summary output after each run

## What stays source-only

These items should remain local/source concerns for now and only be transformed later if a platform can use them:

- `REQUEST_PATTERNS.md`
- `ROUTING.md`
- `STARTER_WORKFLOW.md`
- `templates/`
- source-only metadata like `depends_on` and `handoff_to`

## What exporters should do later

1. read all skills from `skills/qml/`
2. validate frontmatter
3. copy supported files into target platform paths
4. optionally rename or remap support directories
5. inject platform-specific metadata only at export time

## Near-term plan

1. normalize frontmatter in all `SKILL.md` files
2. keep `skills/qml/` as the source-of-truth
3. implement OpenCode export first
4. reuse the same source library for Claude Code and Antigravity
