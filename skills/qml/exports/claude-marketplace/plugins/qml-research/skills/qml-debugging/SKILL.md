---
name: qml-debugging
description: Diagnostic skill for identifying and categorizing failures in PennyLane plus PyTorch QML workflows.
category: debugging
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - qml-pytorch-router
handoff_to:
  - pennylane-qnn
  - qml-pytorch-interface
  - qml-pytorch-training
  - qml-pytorch-performance-patterns
  - pennylane-qiskit-backends
  - qml-cross-framework-benchmarking
---

# qml-debugging

## Purpose

Use this skill when a PennyLane + PyTorch QML workflow is broken, unstable, or producing misleading results, and the first problem is to diagnose what layer is failing before applying a fix. The goal is to identify the failure class, gather evidence, and hand the issue off to the correct implementation skill instead of guessing or changing multiple layers at once.

## Use this skill when

- a QNode fails at runtime
- tensor shapes or measurement outputs do not match the loss path
- gradients are zero, NaN, unstable, or suspiciously tiny
- training does not learn even though code appears to run
- shot-based runs behave inconsistently compared with simulator expectations
- Qiskit-backed execution behaves differently from local PennyLane runs
- you need to decide whether the real issue is model, interface, training, performance, or backend

## Do not use this skill when

- the task is already clearly a model redesign; use `pennylane-qnn`
- the task is already clearly a PyTorch boundary cleanup; use `qml-pytorch-interface`
- the task is already clearly a training-loop redesign; use `qml-pytorch-training`
- the task is already clearly a runtime optimization problem on a correct model; use `qml-pytorch-performance-patterns`
- the task is already clearly a backend extension or backend setup issue; use `pennylane-qiskit-backends`
- the task is only about fair evaluation across working branches; use `qml-cross-framework-benchmarking`

## Required inputs

Before applying this skill, identify:

- the failing code path or failing stage
- the current device/backend and shot configuration
- input, output, and target shapes
- current loss function and optimizer path
- whether the problem appears in local PennyLane only, Qiskit-backed only, or both
- any concrete error messages, warnings, or suspicious metrics

## Core rules

1. **Diagnose before changing architecture.**
2. **Change one layer at a time.**
3. **Always collect evidence before routing to another skill.**
4. **Do not confuse non-learning with performance problems.**

## Decision rules

### Shape and output failures

- If the output shape, target shape, or measurement structure is wrong, route next to `qml-pytorch-interface` or `pennylane-qnn` depending on whether the failure is at the circuit boundary or the model definition.

### Gradient and trainability failures

- If gradients are zero, NaN, or unstable, first confirm that the parameter path is valid and the loss is scalar.
- If the parameter path is correct but the model remains untrainable, treat barren plateau risk or ansatz/cost design as a likely model issue and hand off to `pennylane-qnn`.
- If the training loop mixes multiple uncontrolled changes, route next to `qml-pytorch-training`.

### Runtime and instability failures

- If code is correct but slow, do not use this skill as the final owner; hand off to `qml-pytorch-performance-patterns` after correctness is confirmed.
- If shot-based instability or backend-only weirdness appears, hand off to `pennylane-qiskit-backends` after collecting evidence.

### Benchmark escalation

- If two implementations both work but disagree in ways that need controlled comparison, hand off to `qml-cross-framework-benchmarking`.

## Implementation guidance

### Recommended debugging sequence

1. Confirm the exact failing stage: model, interface, training, performance, or backend.
2. Record shapes, backend, shot count, and loss expectations.
3. Reduce the failure to the smallest reproducible path.
4. Decide whether the issue is structural, interface-level, training-level, runtime-level, or backend-level.
5. Hand off to one primary owner skill with a concrete diagnosis summary.

### Recommended diagnostic output

When using this skill, produce:

- failure class
- evidence collected
- likely root cause
- recommended next owner skill
- what not to change yet

### Minimum failure classes

- `shape-mismatch`
- `measurement-mismatch`
- `gradient-failure`
- `non-learning-training`
- `backend-difference`
- `shot-instability`
- `performance-misdiagnosis`

## Pitfalls to avoid

- changing ansatz, optimizer, and backend together while debugging
- treating low accuracy alone as proof of a model bug
- benchmarking a failing implementation instead of diagnosing it
- confusing shot noise with deterministic shape or logic errors
- routing every broken workflow straight to `qml-pytorch-training`

## Verification checklist

- failing stage is identified explicitly
- evidence includes shapes, backend, and error or metric symptoms
- likely root cause is stated
- one primary next-owner skill is selected
- unnecessary secondary changes are deferred

## Output standard

When this skill is applied well, the result should turn a vague “it is broken” report into a specific diagnosis with a clear next owner and minimal guesswork.
