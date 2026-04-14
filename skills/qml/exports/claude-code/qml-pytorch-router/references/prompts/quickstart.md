# qml-pytorch-router quickstart prompts

## Prompt 1 — route an ambiguous PyTorch QML task

Read this PennyLane + PyTorch QML request and decide which skill should own it first: `pennylane-qnn`, `qml-pytorch-interface`, `qml-pytorch-training`, or `pennylane-qiskit-backends`. Return the primary owner, the routing reason, and any secondary skill only if it becomes relevant later.

## Prompt 2 — identify the first blocking owner

This task touches multiple parts of a PennyLane + PyTorch workflow. Identify the first blocking concern—model architecture, PyTorch integration, training loop, or Qiskit backend support—and route it to the correct skill before implementation begins.
