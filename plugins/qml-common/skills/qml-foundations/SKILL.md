---
name: qml-foundations
description: Grounding skill for framing quantum machine learning problems before implementation.
category: foundations
maturity: core
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on: []
handoff_to:
  - qml-pytorch-router
  - pennylane-qnn
---

# qml-foundations

## Purpose

Use this skill to frame a quantum machine learning problem before implementation begins. The goal is to decide whether the task is actually a good fit for QML, identify the most plausible modeling route, and set realistic success criteria before anyone starts writing circuits, training loops, or benchmark claims.

## Use this skill when

- A new QML idea needs scoping.
- You need to decide between variational, kernel-based, or classical-first approaches.
- You want to define the baseline, metrics, and hardware/simulator assumptions.
- You are translating a research paper or project idea into an implementation plan.

## Do not use this skill when

- The problem framing is already fixed and you only need implementation details.
- The task is purely about optimizer migration, backend switching, or code cleanup.
- The work is purely native Qiskit ML interop.

## Required inputs

Before applying this skill, identify:

- task type and dataset shape
- target metric and failure tolerance
- simulator vs hardware intent
- expected scale of qubits, layers, and shots
- required classical baseline

## Core rules

1. **Do not assume QML is justified by default.**
2. **Always define at least one classical baseline.**
3. **Treat backend, metric, and runtime constraints as part of the model definition.**

## Decision rules

### Choosing the modeling family

- Use variational models when trainable circuits and hybrid optimization are the main research object.
- Use kernel methods when feature-space comparison is more natural than circuit-output training.
- Stay classical-first when data scale, latency, or evaluation constraints make QML unrealistic.

### Choosing the execution target

- Use simulators for rapid iteration and ablation work.
- Add shot-based or remote backends only when the experimental question requires them.

## Implementation guidance

### Recommended migration sequence

1. Define the task and metric.
2. Define the classical baseline.
3. Choose the QML family only if it adds a meaningful experiment.
4. Choose simulator or backend strategy.
5. Freeze a fair comparison plan before implementation starts.

### Recommended code-shape pattern

- separate problem framing from circuit implementation
- keep benchmark assumptions visible in config or notes
- tie every experiment to a baseline and metric plan

## Pitfalls to avoid

- claiming “quantum advantage” from toy experiments
- choosing a quantum method before defining the baseline
- mixing model changes and benchmark changes in one step
- ignoring shot count, runtime, or data scale in evaluation claims

## Verification checklist

- the task objective is explicit
- a classical baseline is defined
- a QML family is chosen for a reason, not trend-following
- simulator/backend assumptions are recorded
- evaluation metrics and comparison rules are fixed up front

## Output standard

When this skill is applied, the result should be a crisp problem framing that makes later implementation decisions obvious instead of speculative.
