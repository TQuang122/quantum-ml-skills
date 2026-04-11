# QML Starter Templates

This directory contains starter code skeletons for the core implementation skills in the QML library.

These templates are intentionally small and modular. They are not full applications; they are clean starting points that match the library's PennyLane-first, PyTorch-first architecture.

## Included templates

- `pennylane-qnn/` — starter model structure for variational classifiers and modular QNodes
- `qml-pytorch-interface/` — starter Torch-facing wrappers and parameter boundaries for PennyLane models
- `qml-pytorch-training/` — starter training loop, metrics, and config flow
- `pennylane-qiskit-backends/` — starter backend configuration and device-switching skeleton

## How to use

1. Pick the template that matches the first blocking concern.
2. Copy it into a real project module.
3. Replace placeholder logic and TODO markers with task-specific code.
4. Keep the interfaces small so later router decisions remain clean.

## Relationship to skills

- Use `pennylane-qnn` when the model/circuit is the main concern.
- Use `qml-pytorch-interface` when Torch integration boundaries are the main concern.
- Use `qml-pytorch-training` when training workflow is the main concern.
- Use `pennylane-qiskit-backends` when execution backends are the main concern.

If the request is ambiguous, use `qml-pytorch-router` before choosing a template.
