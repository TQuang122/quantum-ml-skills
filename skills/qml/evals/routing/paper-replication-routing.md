# Gold Task: Paper Replication Routing

## Task

User request:

> “Implement the main result from this QML paper and compare it against the reported baseline.”

## Expected primary skill

- `qml-paper-replication`

## Expected secondary skill

- `pennylane-qnn`

## Why this routing is correct

The first blocking concern is translating the paper into an implementation and evaluation plan before coding the model.

## Expected output shape

- paper-replication owner
- extracted next-step handoff
- baseline and deviation discipline

## Common failure modes

- routing straight to `pennylane-qnn`
- skipping baseline replication planning

## Pass criteria

- selects `qml-paper-replication`
- mentions assumptions, baselines, or deviations explicitly
