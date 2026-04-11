# Starter Workflow: User Request → Router → Skill → Execution Plan

This file shows the default flow for handling practical requests inside the QML skill library.

## Step 1 — Read the user request

Extract four things immediately:

1. what outcome the user wants
2. whether the model already exists
3. whether the issue is about model structure, PyTorch integration, training, or backend
4. whether Qiskit is only a backend requirement or something broader

## Step 2 — Decide whether routing is needed

Use `qml-pytorch-router` if the request is ambiguous.

Typical router triggers:

- “my code is messy”
- “training is bad”
- “add Qiskit support” plus other refactors
- “fix this workflow” without clear ownership

Skip the router if the correct owner is already obvious.

## Step 3 — Select the primary owner skill

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

**Primary owner:** `qml-pytorch-interface`

**Reason:** the first blocking issue is messy Torch-facing integration; better logs come after the interface is cleaned up.

**Next likely skill:** `qml-pytorch-training`

### Example B

**User request:** “Keep my PennyLane model but add Qiskit-backed execution.”

**Router decision:** skip router if already obvious, or use it and route to `pennylane-qiskit-backends`.

**Primary owner:** `pennylane-qiskit-backends`

**Reason:** the model is stable and the first blocking concern is the execution backend.

## Rule of thumb

If you are unsure, route to the skill that addresses the **earliest unresolved layer** in this stack:

1. model
2. PyTorch interface
3. training loop
4. backend

That ordering prevents late-stage concerns from forcing premature architectural changes.
