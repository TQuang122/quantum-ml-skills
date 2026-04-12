# Gold Task: Reproducibility Research Workflow

## Task

User request:

> “I need this benchmark run to be reproducible across reruns and another machine.”

## Expected primary skill

- `qml-reproducibility`

## Expected secondary skill

- `qml-cross-framework-benchmarking`

## Why this routing is correct

The benchmark cannot be trusted until reproducibility discipline is locked down.

## Expected output shape

- reproducibility owner
- metadata/seeds/splits/backend capture requirements

## Common failure modes

- routing directly to benchmarking
- treating a single seed as enough

## Pass criteria

- selects `qml-reproducibility`
- names the minimum reproducibility artifacts explicitly
