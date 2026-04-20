# qml-pytorch-router example workflows

## Example 1 — route to `pennylane-qnn`

- Input: “Refactor my variational classifier ansatz and measurement layout.”
- Skill outcome: routes to `pennylane-qnn` because the main issue is circuit/model structure.

## Example 2 — route to `qml-pytorch-interface`

- Input: “My PennyLane circuit works, but the Torch tensor and parameter flow is messy.”
- Skill outcome: routes to `qml-pytorch-interface` because the main issue is the PyTorch-facing integration boundary.

## Example 3 — route to `qml-pytorch-training`

- Input: “The model runs, but I need a cleaner optimizer loop with validation and logging.”
- Skill outcome: routes to `qml-pytorch-training` because the forward path is stable and the real issue is training structure.

## Example 4 — route to `pennylane-qiskit-backends`

- Input: “Keep my PennyLane model, but let it run on Qiskit-backed simulators or IBM-oriented backends.”
- Skill outcome: routes to `pennylane-qiskit-backends` because the task is about execution backend extension, not model or training design.
