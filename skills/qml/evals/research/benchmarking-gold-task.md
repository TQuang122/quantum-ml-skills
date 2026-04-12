# Gold Task: Benchmarking Research Workflow

## Task

User request:

> “Compare my PennyLane + PyTorch run against a Qiskit-backed run and tell me whether the benchmark is fair.”

## Expected primary skill

- `qml-cross-framework-benchmarking`

## Expected secondary skill

- `qml-reproducibility`

## Why this routing is correct

The implementation branches already exist; the main task is evaluation discipline and fair comparison.

## Expected output shape

- benchmarking owner
- fairness criteria
- controlled comparison requirements

## Common failure modes

- routing back to implementation without checking whether the evaluation setup is already the main issue
- ignoring seed, backend, or shot metadata

## Pass criteria

- selects `qml-cross-framework-benchmarking`
- lists what must stay constant during comparison
