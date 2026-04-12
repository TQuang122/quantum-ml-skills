# Gold Task: Paper Replication Research Workflow

## Task

User request:

> “Replicate the main result from this QML paper, including the baseline, and tell me whether the final result is really replicated or only approximated.”

## Expected primary skill

- `qml-paper-replication`

## Expected secondary skill

- `qml-reproducibility`

## Why this routing is correct

The first problem is turning the paper into an auditable implementation plan; reproducibility comes next.

## Expected output shape

- extracted assumptions
- missing details
- baseline plan
- verdict criteria

## Common failure modes

- skipping baseline replication
- claiming full replication without a deviation log

## Pass criteria

- selects `qml-paper-replication`
- includes verdict language such as `replicated`, `approximated`, or `unresolved`
