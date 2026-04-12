# Gold Task: Qiskit Backend Implementation

## Task

User request:

> “Keep the same PennyLane model, but let it run on Qiskit-backed simulators and record shot settings explicitly.”

## Expected primary skill

- `pennylane-qiskit-backends`

## Why this routing is correct

The first blocking concern is execution backend extension, not model redesign or training-loop changes.

## Expected output shape

- backend owner
- backend selection scope
- shot-config awareness

## Common failure modes

- routing to `qml-pytorch-interface`
- rewriting the model into native Qiskit unnecessarily

## Pass criteria

- selects `pennylane-qiskit-backends`
- preserves PennyLane-first architecture
