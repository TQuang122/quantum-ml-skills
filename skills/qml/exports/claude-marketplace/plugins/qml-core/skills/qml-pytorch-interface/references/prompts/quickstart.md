# qml-pytorch-interface quickstart prompts

## Prompt 1 — make a PennyLane model PyTorch-first

Refactor this PennyLane circuit path so PyTorch becomes the default tensor and training interface. Keep PennyLane as the circuit layer, make parameter ownership explicit, and preserve numerical behavior before changing the optimizer or backend.

## Prompt 2 — clean up notebook tensor boundaries

Starting from this notebook-based variational classifier, make the Torch tensor boundaries explicit, isolate the QNode, and prepare the code for a cleaner PyTorch training loop.

## Router hint

If the request may actually be about model architecture or training-loop design rather than Torch-facing boundaries, use `qml-pytorch-router` before choosing this skill.
