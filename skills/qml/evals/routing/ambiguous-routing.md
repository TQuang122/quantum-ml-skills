# Gold Task: Ambiguous Routing

## Task

User request:

> “My variational classifier works, but the code is messy and training logs are confusing.”

## Expected primary skill

- `qml-pytorch-router`

## Expected secondary skill

- `qml-debugging` or `qml-pytorch-interface`

## Why this routing is correct

The request is ambiguous and overlaps interface cleanup, training workflow, and possible diagnostic work. The router should own the first move instead of jumping directly into a leaf skill.

## Expected output shape

- primary owner skill
- reason for routing
- optional secondary owner
- narrow scope boundary

## Common failure modes

- routing directly to `qml-pytorch-training` without acknowledging ambiguity
- routing directly to `pennylane-qnn` even though the model is not the stated problem

## Pass criteria

- selects `qml-pytorch-router`
- explains ambiguity clearly
- does not overcommit to implementation too early
