# Gold Task: Debugging Research Workflow

## Task

User request:

> “Training runs without crashing, but the loss does not move and gradients are nearly zero.”

## Expected primary skill

- `qml-debugging`

## Expected secondary skill

- `pennylane-qnn`

## Why this routing is correct

The workflow needs diagnosis first; the likely next owner is model design if trainability is the real issue.

## Expected output shape

- failure class
- evidence to collect
- recommended next owner

## Common failure modes

- routing straight to training redesign
- assuming optimization tweaks alone will solve the issue

## Pass criteria

- selects `qml-debugging`
- identifies diagnosis-before-fix discipline
