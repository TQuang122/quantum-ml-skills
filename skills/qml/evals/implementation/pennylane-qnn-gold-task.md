# Gold Task: PennyLane QNN Implementation

## Task

User request:

> “Refactor my variational classifier ansatz and measurement logic, but keep the overall task and metrics the same.”

## Expected primary skill

- `pennylane-qnn`

## Why this routing is correct

The request is explicitly about model structure: ansatz and measurement logic.

## Expected output shape

- model-structure owner
- in-scope changes limited to encoding/ansatz/measurement/model organization

## Common failure modes

- routing to interface or training instead of model structure
- proposing backend changes when the model itself is the concern

## Pass criteria

- selects `pennylane-qnn`
- protects model-scope boundaries clearly
