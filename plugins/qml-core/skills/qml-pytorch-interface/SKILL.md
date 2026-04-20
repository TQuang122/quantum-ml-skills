---
name: qml-pytorch-interface
description: PyTorch-facing interface skill for clean tensor, parameter, and prediction boundaries around PennyLane models.
category: interface
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - pennylane-qnn
handoff_to:
  - qml-pytorch-training
  - pennylane-qiskit-backends
---

# qml-pytorch-interface

## Purpose

Use this skill when extending a PennyLane-first QML codebase through PyTorch. The goal is to keep PennyLane responsible for circuit definition and backend orchestration, while PyTorch handles tensors, optimizer-compatible parameters, batching, and the broader hybrid-model training interface.

This skill is especially appropriate for variational classifiers, data-reuploading models, and notebook-based QML experiments that need to become cleaner, more modular, and easier to train with the stack already present in this repo.

## Use this skill when

- The project already uses PennyLane and should continue to do so.
- You want to keep PyTorch as the primary tensor and training interface.
- You want a clean bridge between QNodes and PyTorch-friendly model code.
- You need a migration path from notebook experimentation to reusable module-style code.
- You want parameter and prediction boundaries that will still work with later Qiskit backend support.

## Do not use this skill when

- The task is only about switching quantum execution backends; use `pennylane-qiskit-backends` instead.
- The task is only about training-loop structure and optimizer policy; combine with `qml-pytorch-training`.
- The task explicitly requires a native Qiskit ML branch.

## Required inputs

Before applying this skill, identify:

- current device and backend
- current input tensor shape and label format
- model type (variational classifier, data reuploading, etc.)
- parameter shape and initialization scheme
- desired batching behavior
- target metrics and evaluation boundaries

## Core rules

1. **Keep PennyLane as the quantum abstraction.**
   - Define circuits with PennyLane QNodes.
   - Do not turn PyTorch into the quantum authoring layer.

2. **Use PyTorch tensors consistently in the training path.**
   - Avoid mixing `pennylane.numpy`, standard NumPy, and Torch tensors in uncontrolled ways.

3. **Make parameter ownership explicit.**
   - Trainable values should be easy to locate, initialize, inspect, and pass through the model.

4. **Separate circuit logic from training logic.**
   - The QNode should not own the whole training workflow.

5. **Preserve future backend flexibility.**
   - Interface design should not hard-code assumptions that block later Qiskit-backed execution.

## Decision rules

### Selecting the interface path

- Use a PyTorch-first path when the repo already depends on Torch and no compelling reason exists to migrate interfaces.
- Keep the interface simple: one model path, one parameter path, one prediction path.

### Selecting tensor boundaries

- Convert inputs explicitly at the model boundary.
- Avoid repeated Torch↔NumPy conversions inside tight loops.
- Keep output shapes predictable and aligned with the loss function.

### Selecting model structure

- Start from a clean variational-classifier path.
- Add classical pre/post-processing layers only when the experiment actually needs them.

## Implementation guidance

### Recommended migration sequence

1. Isolate the current QNode.
2. Make parameter shapes explicit.
3. Define a clear prediction function or model wrapper.
4. Make batch input handling explicit.
5. Validate forward behavior before changing the training loop.
6. Only then build a fuller PyTorch training path.

### Recommended code-shape pattern

- `init_params(...)`
- `qnode(params, x)` for circuit logic only
- `predict(params, batch)` or a light model wrapper for inference
- loss and evaluation utilities outside the QNode
- training loop separated from circuit definition

### Good boundaries

- circuit definition: PennyLane
- tensors, batches, optimizers: PyTorch
- backend switching: separate concern, not mixed into the interface skill

## Pitfalls to avoid

- mixing Torch tensors and NumPy arrays unpredictably
- hiding trainable parameters inside notebook state
- coupling the QNode too tightly to one training loop
- changing interface, backend, and optimizer simultaneously
- forcing a deep `nn.Module` architecture when a simpler wrapper is enough

## Verification checklist

- QNode behavior is preserved after the PyTorch-first refactor
- inputs and parameters have consistent tensor handling
- forward output shape matches the intended loss path
- batch prediction is explicit and testable
- training concerns remain outside the circuit definition
- the design still supports later backend switching and fair benchmarking

## Output standard

When this skill is applied, the resulting solution should keep PennyLane central while making PyTorch the clean, default path for hybrid QML model interaction.
