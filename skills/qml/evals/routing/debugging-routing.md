# Gold Task: Debugging Routing

## Task

User request:

> “My training gives NaN after a few steps and I do not know whether the model or training loop is wrong.”

## Expected primary skill

- `qml-debugging`

## Expected secondary skill

- `qml-pytorch-training`

## Why this routing is correct

The first blocking concern is diagnosis. The request should not jump straight to training-loop redesign before identifying the failure class.

## Expected output shape

- diagnosis-first owner
- likely next owner after diagnosis
- evidence to collect

## Common failure modes

- routing directly to `qml-pytorch-training`
- treating NaN as only an optimizer problem

## Pass criteria

- selects `qml-debugging`
- names evidence collection as part of the plan
