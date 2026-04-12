# Gold Task: PyTorch Training Implementation

## Task

User request:

> “The forward path works. I need a reusable training loop with validation, logging, and reproducibility controls.”

## Expected primary skill

- `qml-pytorch-training`

## Why this routing is correct

The model and interface are already defined; the core problem is training workflow structure.

## Expected output shape

- training owner
- clear train/validation/logging/reproducibility scope

## Common failure modes

- routing to debugging even though the workflow is not broken
- routing to reproducibility as the sole owner when training structure is still missing

## Pass criteria

- selects `qml-pytorch-training`
- treats reproducibility as part of training hygiene, not a replacement for training design
