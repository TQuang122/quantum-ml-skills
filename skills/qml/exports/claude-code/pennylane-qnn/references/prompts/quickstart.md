# pennylane-qnn quickstart prompts

## Prompt 1 — build a variational classifier

Implement a PennyLane-first variational classifier for this dataset. Separate input encoding, variational block, QNode, prediction, loss, and evaluation so the model can later support PyTorch-first training and Qiskit backend extensions.

## Prompt 2 — refactor notebook code

Refactor this PennyLane notebook into a cleaner module structure. Preserve behavior while making parameter shapes, circuit composition, and evaluation logic explicit.

## Router hint

If it is unclear whether the request is really about model structure or instead about PyTorch integration, training-loop cleanup, or backend execution, run `qml-pytorch-router` first.
