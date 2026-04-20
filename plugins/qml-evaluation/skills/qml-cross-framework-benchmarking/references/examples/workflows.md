# qml-cross-framework-benchmarking example workflows

## Example 1 — migration decision after refactoring to a cleaner PyTorch path

- Input: old notebook-style PennyLane path and new PennyLane + PyTorch training path
- Skill outcome: produces a fair table of accuracy, runtime, and experiment metadata before any architecture decision is made

## Example 2 — compare backend changes safely

- Input: same model evaluated on local simulator and Qiskit-backed execution
- Skill outcome: keeps backend metadata and shot settings visible so result differences are interpretable
