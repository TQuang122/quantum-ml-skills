# Template: qml-pytorch-interface

Starter skeleton for the Torch-facing integration layer around a PennyLane model.

## Files

- `src/interface.py` — input/target normalization helpers
- `src/hybrid_model.py` — lightweight `nn.Module` wrapper around a PennyLane QNode

## Use this template when

- the circuit already exists but PyTorch integration boundaries are unclear
- you need a cleaner parameter and prediction path before touching the training loop

## Next skill to consult

- `qml-pytorch-interface`
- optionally `qml-pytorch-training` once the forward interface is stable
