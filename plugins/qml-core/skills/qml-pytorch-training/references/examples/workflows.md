# qml-pytorch-training example workflows

## Example 1 — replace ad hoc optimizer cells

- Input: notebook uses local optimizer calls and hidden state
- Skill outcome: creates a clearer PyTorch-first training loop with explicit logging and validation

## Example 2 — compare against older baseline fairly

- Input: original PennyLane notebook plus a refactored PyTorch branch
- Skill outcome: preserves matched seeds, metrics, and runtime reporting for a fair training comparison

## Router cross-link

- If the request says “training is bad” but also proposes changing the ansatz or backend, route through `qml-pytorch-router` first to identify the first blocking owner.
