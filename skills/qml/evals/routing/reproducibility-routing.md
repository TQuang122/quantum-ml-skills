# Gold Task: Reproducibility Routing

## Task

User request:

> “The same experiment gives different results on another machine. I need to lock down the run before benchmarking.”

## Expected primary skill

- `qml-reproducibility`

## Expected secondary skill

- `qml-cross-framework-benchmarking`

## Why this routing is correct

The first blocking concern is reproducibility discipline, not benchmarking itself.

## Expected output shape

- primary owner
- reproducibility reason
- what metadata must be captured

## Common failure modes

- routing directly to benchmarking
- routing to debugging without recognizing config/environment drift

## Pass criteria

- selects `qml-reproducibility`
- delays benchmarking until reproducibility is locked down
