# qml-pytorch-performance-patterns example workflows

## Example 1 — batch throughput bottleneck

- Input: correct PennyLane + PyTorch model but slow training over many samples
- Skill outcome: improves batching and measurement discipline without changing the model semantics

## Example 2 — misleading runtime comparison

- Input: one branch reports a speedup after several unrelated refactors
- Skill outcome: isolates the real performance change before any conclusion is accepted
