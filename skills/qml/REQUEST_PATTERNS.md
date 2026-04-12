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
| “why is my training NaN?” | `qml-debugging` | the first need is diagnosis, not immediate training-loop redesign |
| “my circuit gives the wrong shape” | `qml-debugging` | this is a failure-analysis problem before choosing model or interface fixes |
| “the model runs but does not learn” | `qml-debugging` | non-learning runs need diagnosis before changing model or training code |
| “Qiskit backend behaves differently” | `qml-debugging` | backend-specific differences should be diagnosed before changing the backend integration |
| “make this experiment reproducible” | `qml-reproducibility` | the first need is reproducibility discipline, not a model or training rewrite |
| “same code gives different results” | `qml-reproducibility` | environment, split, or metadata drift should be checked before assuming a code bug |
| “lock down my benchmark settings” | `qml-reproducibility` | benchmarking depends on reproducible inputs before fair comparison can begin |
| “implement this paper” | `qml-paper-replication` | the first need is to translate the paper into a concrete implementation plan |
| “replicate the results from this paper” | `qml-paper-replication` | this is a paper-replication workflow before model or training implementation |
| “paper claims X, verify this” | `qml-paper-replication` | the main problem is evaluating fidelity to a paper claim |
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

## Debugging triggers that should route to `qml-debugging`

Use the debugging skill first when the request contains phrases like:

- “NaN”
- “wrong shape”
- “does not learn”
- “gradients are zero”
- “backend behaves differently”
- “QNode fails”

## Reproducibility triggers that should route to `qml-reproducibility`

Use the reproducibility skill first when the request contains phrases like:

- “reproducible”
- “same code, different result”
- “record config”
- “seed policy”
- “lock down benchmark settings”
- “capture backend and shot settings”

## Paper replication triggers that should route to `qml-paper-replication`

Use the paper-replication skill first when the request contains phrases like:

- “implement this paper”
- “replicate this paper”
- “match the baseline from the paper”
- “paper claims”
- “follow the methodology from”

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
- `qml-debugging/SKILL.md`
- `qml-reproducibility/SKILL.md`
- `qml-paper-replication/SKILL.md`

Use `REQUEST_PATTERNS.md` for fast phrase matching. Use `ROUTING.md` for the formal routing map. Use `STARTER_WORKFLOW.md` for the end-to-end process.
