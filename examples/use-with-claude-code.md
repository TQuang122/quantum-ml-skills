# Claude Code Local Marketplace Usage

This is the fastest way to use the repository with a local Claude Code marketplace, and the same plugin bundles can also be published from this repo as a GitHub-hosted marketplace.

## Install the local marketplace

### Project-local marketplace

```bash
bash install/install_claude_marketplace.sh --project-root .
```

### Global marketplace

```bash
bash install/install_claude_marketplace.sh --global
```

Project-local installs go into:

```text
.claude/marketplaces/qml-skills/
```

Global installs go into:

```text
~/.claude/marketplaces/qml-skills/
```

## Validate the marketplace

```bash
python install/doctor_claude_marketplace.py --path .claude/marketplaces/qml-skills
```

## Add the marketplace inside Claude Code

After generating the marketplace, add it from your Claude Code session:

```text
/plugin marketplace add ./.claude/marketplaces/qml-skills
```

## Install recommended plugin bundles

Install the shared bundle first:

```text
/plugin install qml-common@qml-skills
```

Then install the bundles you need:

```text
/plugin install qml-core@qml-skills
/plugin install qml-backends@qml-skills
/plugin install qml-evaluation@qml-skills
/plugin install qml-research@qml-skills
```

Install bundles sequentially. Running multiple install commands in parallel can race on Claude Code's local plugin state.

## Add the marketplace from GitHub

After syncing the hosted marketplace view into the repository root and pushing it to GitHub, users can add the marketplace directly from the repo:

```text
/plugin marketplace add TQuang122/quantum-ml-skills
```

Optional sparse checkout for hosted usage:

```text
/plugin marketplace add TQuang122/quantum-ml-skills --sparse .claude-plugin plugins
```

## Export without installing

If you only want generated marketplace output in the repository:

```bash
python skills/qml/exporters/export_claude_marketplace.py
```

To sync the hosted marketplace view into the repository root for GitHub hosting:

```bash
python skills/qml/exporters/export_claude_marketplace.py --sync-hosted-root
```

Generated output goes to:

```text
skills/qml/exports/claude-marketplace/
```

Hosted marketplace sync writes to:

```text
.claude-plugin/
plugins/
```

## Plugin bundle map

- `qml-common` — foundations and routing
- `qml-core` — PennyLane + PyTorch implementation skills
- `qml-backends` — backend and Qiskit interop skills
- `qml-evaluation` — benchmarking and reproducibility skills
- `qml-research` — debugging and paper replication skills

## Related docs

- `README.md`
- `CLAUDE.md`
- `skills/qml/EXPORT_STRATEGY.md`
- `skills/qml/README.md`
- `install/README.md`
