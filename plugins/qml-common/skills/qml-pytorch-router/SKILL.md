---
name: qml-pytorch-router
description: Meta-skill that routes ambiguous PennyLane plus PyTorch QML requests to the correct implementation skill.
category: routing
maturity: core
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
handoff_to:
  - pennylane-qnn
  - qml-pytorch-interface
  - qml-pytorch-training
  - pennylane-qiskit-backends
---

# qml-pytorch-router

## Purpose

Use this skill when a request clearly belongs inside the PennyLane + PyTorch QML stack, but it is not yet obvious which implementation skill should own the work. The goal is to route the task cleanly to one of four nearby skills:

- `pennylane-qnn`
- `qml-pytorch-interface`
- `qml-pytorch-training`
- `pennylane-qiskit-backends`

This is a meta-skill. It decides **where the work belongs** before implementation starts. It does not replace the leaf skills and should not absorb their responsibilities.

## Use this skill when

- The user has a PennyLane + PyTorch request but the scope is ambiguous.
- A task may involve circuit/model structure, PyTorch integration, training-loop cleanup, or Qiskit backend support, and you need to choose the primary owner.
- You want to avoid overlapping edits across multiple nearby QML skills.
- You need a fast triage layer before deeper implementation.

## Do not use this skill when

- It is already obvious that the task is about model architecture; use `pennylane-qnn`.
- It is already obvious that the task is about PyTorch tensor/model boundaries; use `qml-pytorch-interface`.
- It is already obvious that the task is about optimizer/training-loop structure; use `qml-pytorch-training`.
- It is already obvious that the task is about Qiskit-backed execution or IBM-style backends; use `pennylane-qiskit-backends`.
- The task is about benchmarking or native Qiskit ML interop; use the specialized skills directly.

## Required inputs

Before applying this skill, identify:

- the user’s requested outcome
- whether the task changes circuit/model structure, interface boundaries, training behavior, or execution backend
- whether PyTorch remains the main training interface
- whether Qiskit is being introduced only as a backend or as a separate implementation branch
- whether the task is mostly architectural or mostly operational

## Core rules

1. **Route to one primary skill first.**
   - Do not split a small task across multiple skills unless the user request truly spans multiple concerns.

2. **Prefer the narrowest sufficient owner.**
   - If one leaf skill can fully own the task, route there instead of escalating unnecessarily.

3. **Treat backend work as distinct from interface and training work.**
   - Qiskit backend extension is not the same as PyTorch cleanup or training-loop refactoring.

4. **Keep PennyLane as the architectural center.**
   - Routing should preserve the library’s PennyLane-first design principle.

## Decision rules

### Route to `pennylane-qnn` when

- the main issue is circuit composition
- the task changes encoding, ansatz, measurement, or model structure
- the user is building or refactoring the quantum model itself
- the work is about making the PennyLane model modular and reusable

### Route to `qml-pytorch-interface` when

- the circuit exists, but the PyTorch-facing integration is messy
- tensor boundaries, parameter ownership, or prediction wrappers are unclear
- notebook-style code needs to become a cleaner PyTorch-compatible model path
- the main question is how PennyLane and PyTorch should connect

### Route to `qml-pytorch-training` when

- the forward path is already defined
- the main issue is optimizer choice, batching, training steps, validation, or logging
- notebook optimization code needs to become a reusable training loop
- reproducibility or train/validation discipline is the central concern

### Route to `pennylane-qiskit-backends` when

- the task is about adding Qiskit simulators or IBM-oriented backends
- the model should stay PennyLane-authored while execution targets change
- shot configuration, backend selection, or plugin-backed execution is the main topic

### Escalation rule

- If a request genuinely spans model structure, PyTorch interface, and backend changes at once, choose the **first blocking owner**:
  - model shape unclear → `pennylane-qnn`
  - model shape stable but Torch boundaries unclear → `qml-pytorch-interface`
  - model and interface stable but training unstable → `qml-pytorch-training`
  - model/interface/training stable but execution target changes → `pennylane-qiskit-backends`

## Implementation guidance

### Recommended routing sequence

1. Read the task and name the real problem type.
2. Check whether the main change is model, interface, training, or backend.
3. Assign one primary owner.
4. Only involve a second skill if the first one cannot complete the task cleanly.

### Recommended output pattern

When using this router, produce:

- the selected primary skill
- a one-sentence reason for the selection
- any secondary skill that may be relevant later, if truly needed

### Minimal routing map

- **Model/circuit problem** → `pennylane-qnn`
- **Torch boundary/interface problem** → `qml-pytorch-interface`
- **Optimizer/training loop problem** → `qml-pytorch-training`
- **Qiskit execution/backend problem** → `pennylane-qiskit-backends`

## Pitfalls to avoid

- routing everything to the broadest skill instead of the narrowest one
- confusing PyTorch interface cleanup with training-loop redesign
- treating Qiskit backend support as a model-architecture problem
- routing a task to multiple skills by default when one owner is enough
- bypassing the router when the request is ambiguous and overlap is likely

## Verification checklist

- one primary owner skill is selected
- the routing reason is explicit
- the selected owner matches the task’s first blocking concern
- no unnecessary second skill is introduced
- PennyLane-first architecture is preserved by the routing decision

## Output standard

When this skill is applied well, ambiguous PennyLane + PyTorch requests become easy to hand off to the correct implementation skill without overlap, duplication, or architectural drift.
