# QML Request Patterns

This document maps common user phrasings to the most appropriate skill in the QML library.

Use it as a fast lookup layer before deeper routing. If the correct owner is still unclear after reading a request pattern, use `qml-pytorch-router`.

## Default rule

- **Obvious owner** → route directly to the matching skill
- **Ambiguous or overlapping request** → route to `qml-pytorch-router`

## Phrase-to-skill map

| User phrase or intent pattern | Route to | Why |
|---|---|---|
| “my code is messy” | `qml-pytorch-router` | “messy” is ambiguous and could mean model, interface, training, or backend problems |
| “this workflow is broken” | `qml-pytorch-router` | the failing layer is not yet clear |
| “help me figure out what to fix first” | `qml-pytorch-router` | the request is explicitly about triage |
| “refactor ansatz” | `pennylane-qnn` | ansatz changes belong to model/circuit structure |
| “change the measurement logic” | `pennylane-qnn` | measurement outputs are part of the PennyLane model definition |
| “restructure my variational classifier” | `pennylane-qnn` | the quantum model itself is being reshaped |
| “my QNode works but Torch integration is ugly” | `qml-pytorch-interface` | the model exists and the real issue is the PyTorch-facing boundary |
| “clean up tensor flow” | `qml-pytorch-interface` | tensor ownership and conversion boundaries are the main concern |
| “parameter handling is confusing” | `qml-pytorch-interface` | parameter ownership belongs to the interface layer |
| “training loop bad” | `qml-pytorch-training` | the forward path exists and the pain is in training structure |
| “I need better validation and logging” | `qml-pytorch-training` | validation and logging belong to the training workflow |
| “make this notebook trainer reusable” | `qml-pytorch-training` | the task is about turning notebook optimization into a real training path |
| “speed up this PyTorch QML workflow” | `qml-pytorch-performance-patterns` | the main goal is runtime/performance improvement |
| “batching is too slow” | `qml-pytorch-performance-patterns` | batching throughput is a performance concern |
| “profile this QML training run” | `qml-pytorch-performance-patterns` | profiling and bottleneck analysis belong to the performance skill |
| “add Qiskit backend support” | `pennylane-qiskit-backends` | the execution target is changing while PennyLane remains the authoring layer |
| “run this on IBM-style backends” | `pennylane-qiskit-backends` | the task is explicitly about Qiskit-backed execution |
| “keep the model but switch backend” | `pennylane-qiskit-backends` | backend work is the first blocking concern |
| “compare my PyTorch path against Qiskit-backed runs” | `qml-cross-framework-benchmarking` | the task is evaluation and comparison, not primary implementation |
| “audit whether this benchmark is fair” | `qml-cross-framework-benchmarking` | benchmark fairness is the core concern |
| “should I use native Qiskit ML here?” | `qiskit-machine-learning-interop` | the question is specifically about native Qiskit ML justification |
| “try TorchConnector / EstimatorQNN / SamplerQNN” | `qiskit-machine-learning-interop` | those are native Qiskit ML abstractions |

## Ambiguity triggers that should route to `qml-pytorch-router`

Use the router first when the request contains phrases like:

- “messy”
- “broken”
- “bad”
- “fix this workflow”
- “refactor this whole thing”
- “add Qiskit” plus other refactors
- “clean this up” without naming the layer

## Quick interpretation guide

### Requests that usually mean `pennylane-qnn`

- model shape is changing
- ansatz is changing
- encoding is changing
- measurement is changing

### Requests that usually mean `qml-pytorch-interface`

- Torch-facing wiring is unclear
- parameter ownership is unclear
- tensor conversion boundaries are messy

### Requests that usually mean `qml-pytorch-training`

- optimizer loop needs work
- validation/logging is missing
- notebook training needs to become reusable

### Requests that usually mean `pennylane-qiskit-backends`

- execution target changes
- Qiskit simulator/backend work is the focus
- shot-aware backend behavior matters

## Related docs

- `ROUTING.md`
- `STARTER_WORKFLOW.md`
- `qml-pytorch-router/SKILL.md`

Use `REQUEST_PATTERNS.md` for fast phrase matching. Use `ROUTING.md` for the formal routing map. Use `STARTER_WORKFLOW.md` for the end-to-end process.
