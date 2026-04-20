---
name: pennylane-qnn
description: Core implementation skill for PennyLane-first hybrid quantum neural network models.
category: modeling
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
handoff_to:
  - qml-pytorch-interface
  - qml-pytorch-training
  - pennylane-qiskit-backends
---

# pennylane-qnn

## Purpose

Use this skill to implement or refactor PennyLane-first hybrid quantum neural network code in a clean, reusable way. The goal is to separate circuit definition, parameter handling, training logic, and evaluation so variational classifiers and related models are easy to extend toward PyTorch-first training, Qiskit backends, and fair benchmarking later.

## Use this skill when

- Building a variational classifier in PennyLane.
- Refactoring notebook-based QML prototypes into cleaner code.
- Adding data reuploading, measurement logic, or circuit modularity.
- Keeping PyTorch integration while improving architecture.

## Do not use this skill when

- The main task is PyTorch interface migration details.
- The main task is Optax training-loop design.
- The main task is backend diversification through Qiskit.

## Required inputs

Before applying this skill, identify:

- device and wire count
- input encoding strategy
- ansatz structure and parameter shape
- measurement outputs and label format
- training interface and evaluation metrics

## Core rules

1. **Keep circuit logic separate from training logic.**
2. **Make parameter shapes explicit and stable.**
3. **Design the model so backend or interface changes do not require rewriting the whole circuit.**

## Decision rules

### Circuit structure

- Use simple, inspectable ansatz blocks first.
- Add depth only when justified by the experiment.

### Integration boundary

- Keep PennyLane as the authoring layer.
- Treat PyTorch as the default integration layer and avoid redesigning the circuit just to satisfy the training stack.

## Implementation guidance

### Recommended migration sequence

1. Isolate data encoding.
2. Isolate the variational block.
3. Isolate the QNode.
4. Build prediction and loss functions separately.
5. Add training and evaluation on top.

### Recommended code-shape pattern

- `encode_input(x)`
- `variational_block(params)`
- `qnode(params, x)`
- `predict(params, batch)`
- `loss_fn(...)` and evaluation utilities

## Pitfalls to avoid

- packing all logic into notebook cells
- hiding parameter-shape assumptions inside the circuit body
- changing encoding, ansatz, and optimizer all at once
- making the circuit depend on one training framework too deeply

## Verification checklist

- circuit components are modular
- parameter shapes are explicit
- prediction and loss paths are testable separately
- training/evaluation code does not duplicate circuit logic
- the model can be extended to PyTorch-first training and Qiskit backend work without major rewrite

## Output standard

When this skill is applied, the resulting PennyLane model should be clean enough to serve as the stable center of the broader QML library.
