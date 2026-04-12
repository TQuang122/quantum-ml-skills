# Release Notes — v0.1.1

Patch release focused on **OpenCode hardening** and a major expansion of the QML skill system toward advanced research workflows.

## Highlights

- safer global OpenCode install path using a namespaced directory
- stronger `doctor_opencode.py` validation
- three new advanced QML skills
- a new gold-task eval suite for routing, implementation, and research workflows

## OpenCode hardening

This release strengthens the OpenCode path with:

- safer namespaced global install path:

```text
~/.config/opencode/skills/qml-skills/
```

- shell installer entrypoint:
  - `install/install_opencode.sh`
- stronger doctor checks for:
  - frontmatter presence
  - required metadata keys
  - `name` to folder matching
  - `platforms` coverage for `opencode`
  - expected skill count
  - namespace consistency

## New skills

This release adds:

- `qml-debugging`
- `qml-reproducibility`
- `qml-paper-replication`

These fill major gaps in the original library by covering:

- failure analysis
- rerunnable / auditable experiment discipline
- paper-to-code replication workflows

## New eval suite

This release also adds:

- `skills/qml/evals/`

Initial eval categories:

- `routing/`
- `implementation/`
- `research/`

The suite is lightweight and markdown-first, designed to validate routing quality, skill boundaries, and expected output contracts.

## Current skill count

The library now contains **12 skills**:

- `qml-foundations`
- `qml-pytorch-router`
- `qml-debugging`
- `qml-reproducibility`
- `qml-paper-replication`
- `pennylane-qnn`
- `qml-pytorch-interface`
- `qml-pytorch-training`
- `qml-pytorch-performance-patterns`
- `pennylane-qiskit-backends`
- `qiskit-machine-learning-interop`
- `qml-cross-framework-benchmarking`

## Notes

- OpenCode remains the primary supported platform in this release.
- Claude Code and Antigravity remain source-ready, but their exporters are still not implemented.
- This release is a stronger, more complete public beta for OpenCode users and moves the library closer to an advanced research-oriented QML skill system.

## Quick start

```bash
bash install/install_opencode.sh --project-root .
```

For more usage details, see:

- `README.md`
- `examples/use-with-opencode.md`
- `skills/qml/evals/README.md`
