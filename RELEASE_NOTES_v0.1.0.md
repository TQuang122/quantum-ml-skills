# Release Notes — v0.1.0

Initial public release of **Quantum ML Skills**.

## Highlights

- 9 reusable QML skills built around a PennyLane-first, PyTorch-first workflow
- normalized `SKILL.md` frontmatter for future multi-platform exports
- request routing docs and phrase-to-skill matching
- starter templates for core QML implementation tasks
- OpenCode exporter, installer, shell wrapper, and doctor workflow
- safer namespaced global install path for OpenCode

## Included skills

- `qml-foundations`
- `qml-pytorch-router`
- `pennylane-qnn`
- `qml-pytorch-interface`
- `qml-pytorch-training`
- `qml-pytorch-performance-patterns`
- `pennylane-qiskit-backends`
- `qiskit-machine-learning-interop`
- `qml-cross-framework-benchmarking`

## OpenCode support

This release includes:

- `skills/qml/exporters/export_opencode.py`
- `install/install_opencode.py`
- `install/install_opencode.sh`
- `install/doctor_opencode.py`

Supported flows:

- local project install
- single-skill install
- dry-run validation
- global namespaced install into:

```text
~/.config/opencode/skills/qml-skills/
```

## Repository structure

The repository includes:

- source-of-truth library under `skills/qml/`
- routing and workflow docs
- starter templates
- OpenCode export scaffolding
- GitHub-ready collaboration files under `.github/`

## Notes

- OpenCode is the first platform target implemented in this release.
- Claude Code and Antigravity remain source-level export-ready, but their exporters are not yet implemented.
- This release is best treated as a public beta for OpenCode users.

## Quick start

```bash
bash install/install_opencode.sh --project-root .
```

For more usage details, see:

- `README.md`
- `examples/use-with-opencode.md`
