# pennylane-qnn example workflows

## Example 1 — modularize a data-reuploading notebook

- Input: one notebook mixing preprocessing, circuit logic, and training
- Skill outcome: extracts reusable PennyLane model pieces without changing the core experiment

## Example 2 — prepare for PyTorch-first training

- Input: working PennyLane variational classifier that needs a cleaner Torch training structure
- Skill outcome: keeps circuit authoring stable while reducing coupling to notebook-local training code

## Router cross-link

- If a request mixes ansatz changes with training-loop complaints, route through `qml-pytorch-router` first to decide whether `pennylane-qnn` or `qml-pytorch-training` should own the first move.
