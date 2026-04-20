# qml-pytorch-training quickstart prompts

## Prompt 1 — build a reusable PyTorch training loop

Create a PennyLane + PyTorch training loop for this variational model. Keep parameters, optimizer setup, batching, validation, and logging explicit, and preserve fair comparison with the current notebook baseline.

## Prompt 2 — turn a notebook into a benchmarkable trainer

Refactor this notebook training flow into a reusable PyTorch-first training path with explicit loss, optimizer, train/validation metrics, and reproducibility controls.

## Router hint

If the task might instead be about Torch integration boundaries or Qiskit backend execution, call `qml-pytorch-router` first and let it choose the primary owner.
