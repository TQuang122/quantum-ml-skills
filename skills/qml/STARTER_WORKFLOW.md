# Starter Workflow: User Request → Router → Skill → Execution Plan

This file shows the default flow for handling practical requests inside the QML skill library.

## Step 1 — Read the user request

Extract four things immediately:

1. what outcome the user wants
2. whether the model already exists
3. whether the issue is about model structure, PyTorch integration, training, debugging, reproducibility, paper replication, or backend
4. whether Qiskit is only a backend requirement or something broader

## Step 2 — Decide whether routing is needed

Use `qml-pytorch-router` if the request is ambiguous.

Typical router triggers:

- “my code is messy”
- “training is bad”
- “add Qiskit support” plus other refactors
- “fix this workflow” without clear ownership

Typical debugging triggers:

- “my training is NaN”
- “this gives the wrong shape”
- “the model runs but does not learn”
- “the backend behaves differently”

Typical reproducibility triggers:

- “same code, different result”
- “make this experiment reproducible”
- “lock down benchmark settings”
- “capture backend and shot settings”

Typical paper-replication triggers:

- “implement this paper”
- “replicate these results”
- “match the baseline from the paper”
- “paper claims X”

Skip the router if the correct owner is already obvious.

## Step 3 — Select the primary owner skill

### Route to `qml-debugging` when

- the failing layer is unclear
- the workflow is broken and diagnosis comes before the fix
- gradients, shapes, outputs, or backend behavior look suspicious

### Route to `qml-reproducibility` when

- the workflow runs, but results need to be rerunnable and auditable
- the same experiment gives different outcomes across reruns or machines
- benchmarking cannot start until split, config, backend, and shot settings are locked down

### Route to `qml-paper-replication` when

- the task begins from a paper or publication claim
- the main issue is extracting assumptions and mapping the paper to code
- the team needs a verdict on whether results are replicated or only approximated

### Route to `pennylane-qnn` when

- the task changes encoding
- the task changes ansatz
- the task changes measurement outputs
- the task restructures the PennyLane model itself

### Route to `qml-pytorch-interface` when

- the model works but Torch integration is messy
- tensor boundaries are unclear
- parameter ownership or prediction wrappers need cleanup

### Route to `qml-pytorch-training` when

- the forward path exists
- the training loop is the problem
- the user needs batching, optimizer structure, validation, or logging

### Route to `pennylane-qiskit-backends` when

- the model should remain PennyLane-authored
- the execution backend is changing to Qiskit-backed paths
- the issue is simulator/backend configuration or shot-aware execution

## Step 4 — Write the execution plan

After the owner skill is selected, the execution plan should contain:

1. **Primary owner skill**
2. **Reason for routing**
3. **Scope boundary**
4. **Expected deliverables**
5. **Validation requirements**

### Minimal execution-plan template

```text
Primary owner: <skill-name>
Reason: <one sentence>
In scope: <what this skill should change>
Out of scope: <what it should not change yet>
Validation: <what evidence proves success>
```

## Example end-to-end flow

### Example A

**User request:** “My variational classifier works but the code is tangled and I also want better training logs.”

**Router decision:** `qml-pytorch-router`

**Primary owner:** `qml-debugging`

**Reason:** the first blocking issue is not yet clear; the workflow mixes symptoms across interface and training.

**Next likely skill:** `qml-pytorch-interface` or `qml-pytorch-training`

### Example B

**User request:** “Keep my PennyLane model but add Qiskit-backed execution.”

**Router decision:** skip router if already obvious, or use it and route to `pennylane-qiskit-backends`.

**Primary owner:** `pennylane-qiskit-backends`

**Reason:** the model is stable and the first blocking concern is the execution backend.

### Example C

**User request:** “The same experiment gives different results on another machine, and I need to make the benchmark reproducible.”

**Router decision:** `qml-pytorch-router`

**Primary owner:** `qml-reproducibility`

**Reason:** the first blocking concern is experiment reproducibility rather than model redesign or training-loop changes.

### Example D

**User request:** “I want to reproduce the main classifier result from this QML paper and compare it against the reported baseline.”

**Router decision:** `qml-pytorch-router`

**Primary owner:** `qml-paper-replication`

**Reason:** the first blocking concern is translating the paper into an auditable implementation and evaluation plan.

## Rule of thumb

If you are unsure, route to the skill that addresses the **earliest unresolved layer** in this stack:

1. model
2. debugging
3. reproducibility
4. paper replication
5. PyTorch interface
6. training loop
7. backend

That ordering prevents late-stage concerns from forcing premature architectural changes.
