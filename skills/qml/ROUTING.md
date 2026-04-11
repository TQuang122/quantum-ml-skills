# QML Skill Routing Guide

This document is the shared routing layer for the QML skill library.

Use it when a request clearly belongs inside the PennyLane + PyTorch QML stack, but you need to decide **which skill should own the first implementation move**.

## Routing principle

Choose the **first blocking owner**, not the broadest possible owner.

That means:

- route to the skill that must act first for the task to make progress
- do not split a request across multiple skills unless the overlap is real and unavoidable
- keep PennyLane as the architectural center

## Primary routing map

| If the main problem is... | Route to... | Why |
|---|---|---|
| circuit composition, ansatz, encoding, measurement, model structure | `pennylane-qnn` | the quantum model itself is the first blocking concern |
| Torch tensor boundaries, parameter ownership, prediction wrappers, interface cleanup | `qml-pytorch-interface` | the model exists, but the PyTorch-facing integration is unstable or unclear |
| optimizer design, batching, train/validation structure, logging, reproducibility | `qml-pytorch-training` | the forward path is defined and the training workflow is the real bottleneck |
| Qiskit simulators, IBM-oriented execution, plugin-backed backend switching, shot-based backend behavior | `pennylane-qiskit-backends` | the execution target is changing while PennyLane remains the authoring layer |

## Secondary routing rules

### Use `qml-pytorch-router` when

- the request is ambiguous
- the request touches model + interface + training at once
- the user says the code is “messy” or “broken” without clearly naming where the problem lives
- Qiskit is mentioned together with other refactors

### Do not use `qml-pytorch-router` when

- the correct owner is already obvious
- the task is benchmarking-only
- the task is native Qiskit ML interop

## Escalation sequence

If a request touches multiple areas, route by the first blocking concern:

1. **Model unclear** → `pennylane-qnn`
2. **Model clear, Torch boundaries unclear** → `qml-pytorch-interface`
3. **Model + interface clear, training unstable** → `qml-pytorch-training`
4. **Model + interface + training clear, execution target changes** → `pennylane-qiskit-backends`

## Short examples

- “Refactor my ansatz and measurement logic” → `pennylane-qnn`
- “My QNode works but the Torch parameter flow is ugly” → `qml-pytorch-interface`
- “I need batching, validation, and better optimizer structure” → `qml-pytorch-training`
- “Keep the same model but run it on Qiskit-backed simulators” → `pennylane-qiskit-backends`

## Related files

- `qml-pytorch-router/SKILL.md`
- `STARTER_WORKFLOW.md`

Use this routing guide as the library-level summary. Use `qml-pytorch-router` when you need a task-level routing decision.
