# qml-debugging example workflows

## Example 1 — route shape failure to interface work

- Input: “My QNode runs, but the logits shape does not match the target shape.”
- Skill outcome: classifies the issue as `shape-mismatch` and routes next to `qml-pytorch-interface`.

## Example 2 — route non-learning model to model redesign

- Input: “Training runs without crashing, but the loss does not move and gradients are nearly zero.”
- Skill outcome: classifies the issue as `gradient-failure` or `non-learning-training`, gathers evidence, and routes next to `pennylane-qnn` or `qml-pytorch-training` depending on the root cause.

## Example 3 — route backend-only weirdness correctly

- Input: “The local PennyLane simulator behaves fine, but the Qiskit-backed run gives very different behavior.”
- Skill outcome: classifies the issue as `backend-difference` or `shot-instability` and routes next to `pennylane-qiskit-backends`.
