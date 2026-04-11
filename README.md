# Quantum ML Skills

Reusable QML skills with PennyLane-first design, PyTorch-first training, and OpenCode-ready installation.

These skills are designed for OpenCode first, with the source library structured so it can later be exported to other skill-compatible agent systems.

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
- `CONTRIBUTING.md`

## Release

- `CHANGELOG.md`
- `RELEASE_CHECKLIST.md`
- `RELEASE_NOTES_v0.1.0.md`

## License

MIT
