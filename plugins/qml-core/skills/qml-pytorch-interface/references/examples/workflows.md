# qml-pytorch-interface example workflows

## Example 1 — replace mixed array handling

- Input: notebook mixes Torch tensors, NumPy, and PennyLane-specific arrays
- Skill outcome: introduces a clean PyTorch-first parameter and prediction path around the existing QNode

## Example 2 — prepare for backend extension

- Input: working PennyLane classifier tied too closely to one notebook training style
- Skill outcome: keeps the circuit stable while making the PyTorch interface reusable and backend-friendly

## Router cross-link

- If the user says “my model works but the code is messy,” route through `qml-pytorch-router` first to decide whether the mess is really interface-level or training-level.
