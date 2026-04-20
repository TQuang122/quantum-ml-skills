# pennylane-qiskit-backends example workflows

## Example 1 — add IBM-oriented execution safely

- Input: PennyLane variational classifier that currently runs only on local simulators
- Skill outcome: adds configurable Qiskit-backed devices without rewriting the circuit code

## Example 2 — compare simulator paths

- Input: same conceptual circuit on local PennyLane and Qiskit-backed execution
- Skill outcome: records shots, backend metadata, and runtime context for a fair comparison

## Router cross-link

- If a request says “add Qiskit” but the model and Torch integration are still unstable, route through `qml-pytorch-router` first so backend work does not start too early.
