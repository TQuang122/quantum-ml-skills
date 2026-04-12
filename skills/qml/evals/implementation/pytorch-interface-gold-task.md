# Gold Task: PyTorch Interface Implementation

## Task

User request:

> “My QNode works, but Torch tensor flow and parameter ownership are messy.”

## Expected primary skill

- `qml-pytorch-interface`

## Why this routing is correct

The model exists; the issue is the PyTorch-facing integration boundary.

## Expected output shape

- interface owner
- tensor/parameter boundary cleanup scope

## Common failure modes

- routing to model redesign
- routing to training loop before fixing interface boundaries

## Pass criteria

- selects `qml-pytorch-interface`
- clearly focuses on interface-level cleanup
