# pennylane-qiskit-backends quickstart prompts

## Prompt 1 — add Qiskit backend support

Extend this PennyLane-first project with Qiskit-backed execution. Keep the circuit authoring model unchanged, isolate device construction, add explicit shot settings, and benchmark against the current simulator under controlled conditions.

## Prompt 2 — review backend-switch design

Review this proposed PennyLane + Qiskit backend integration and check whether it preserves a PennyLane-first architecture or accidentally forks the repo into competing framework paths.

## Router hint

If the user request mentions Qiskit together with model redesign or training cleanup, run `qml-pytorch-router` first to separate backend work from model/interface/training work.
