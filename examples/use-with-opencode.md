# OpenCode Usage

This is the fastest way to use the repository with OpenCode.

## Install

### Local project

```bash
bash install/install_opencode.sh --project-root .
```

### Global

```bash
bash install/install_opencode.sh --global
```

Global installs go into:

```text
~/.config/opencode/skills/qml-skills/
```

## Single skill

```bash
bash install/install_opencode.sh --project-root . --skill qml-pytorch-training
```

## Dry run

```bash
bash install/install_opencode.sh --project-root . --dry-run
```

## Skills

| Skill | Description |
| --- | --- |
| `qml-foundations` | Frame QML problems before implementation. |
| `qml-pytorch-router` | Route ambiguous PennyLane + PyTorch QML requests. |
| `pennylane-qnn` | Build and refactor PennyLane-first hybrid quantum models. |
| `qml-pytorch-interface` | Clean PyTorch boundaries around PennyLane models. |
| `qml-pytorch-training` | Build reusable PennyLane + PyTorch training workflows. |
| `qml-pytorch-performance-patterns` | Improve performance for PyTorch-based QML workloads. |
| `pennylane-qiskit-backends` | Add Qiskit-backed execution while keeping PennyLane as the authoring layer. |
| `qiskit-machine-learning-interop` | Explore native Qiskit Machine Learning abstractions. |
| `qml-cross-framework-benchmarking` | Compare QML branches and backends fairly. |

## Manual fallback

If you do not want to use the installer, export skills first and copy the generated output manually.

```bash
python skills/qml/exporters/export_opencode.py
```

Generated output goes to:

```text
skills/qml/exports/opencode/
```

## Suggested usage flow

1. check `skills/qml/REQUEST_PATTERNS.md`
2. use `skills/qml/ROUTING.md` if the task is ambiguous
3. start with `qml-pytorch-router` when multiple skills overlap

## Recommended starting skills

- `qml-foundations`
- `qml-pytorch-router`
- `pennylane-qnn`
- `qml-pytorch-training`

## Related docs

- `README.md`
- `skills/qml/README.md`
- `skills/qml/REQUEST_PATTERNS.md`
- `skills/qml/ROUTING.md`
