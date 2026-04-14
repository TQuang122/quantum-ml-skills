# Quantum ML Skills

![Qubit Animation](./qubit.gif)

Reusable QML skills with PennyLane-first design, PyTorch-first training, and exporter-based compatibility for OpenCode and Claude Code.

These skills are maintained from a single source library so they can support OpenCode today and Claude Code through a compatible export layer without splitting the docs or source structure.

## Installation

### OpenCode

Install into a local project:

```bash
bash install/install_opencode.sh --project-root .
```

Install globally:

```bash
bash install/install_opencode.sh --global
```

Global installs go into:

```text
~/.config/opencode/skills/qml-skills/
```

This keeps the skills namespaced and avoids resetting the whole global OpenCode skills root.

If you prefer not to call the shell installer directly, see:

- `examples/use-with-opencode.md`

You can validate an install with:

```bash
python install/doctor_opencode.py --path .opencode/skills
```

### Claude Code

Claude Code support is provided through:

- root `CLAUDE.md`
- project `.claude/settings.json`
- generated exports under `skills/qml/exports/claude-code/`

To generate Claude-compatible output:

```bash
python skills/qml/exporters/export_claude_code.py
```

The canonical source of truth remains:

```text
skills/qml/
```

## Skills

| Skill | Description |
| --- | --- |
| `qml-foundations` | Frame QML problems before implementation. |
| `qml-pytorch-router` | Route ambiguous PennyLane + PyTorch QML requests to the correct implementation skill. |
| `pennylane-qnn` | Build and refactor PennyLane-first hybrid quantum models. |
| `qml-pytorch-interface` | Clean PyTorch tensor, parameter, and prediction boundaries around PennyLane models. |
| `qml-pytorch-training` | Build reusable PennyLane + PyTorch training workflows. |
| `qml-pytorch-performance-patterns` | Improve performance for PyTorch-based QML workloads. |
| `pennylane-qiskit-backends` | Add Qiskit-backed execution while keeping PennyLane as the authoring layer. |
| `qiskit-machine-learning-interop` | Explore native Qiskit Machine Learning abstractions when plugin-backed execution is not enough. |
| `qml-cross-framework-benchmarking` | Compare QML branches and backends fairly. |

## Advanced docs

- `skills/qml/README.md`
- `skills/qml/REQUEST_PATTERNS.md`
- `skills/qml/ROUTING.md`
- `skills/qml/STARTER_WORKFLOW.md`
- `skills/qml/EXPORT_STRATEGY.md`
- `examples/use-with-opencode.md`
- `CLAUDE.md`
- `CONTRIBUTING.md`

## Release

- `CHANGELOG.md`
- `RELEASE_CHECKLIST.md`
- `RELEASE_NOTES_v0.1.0.md`

## License

MIT
