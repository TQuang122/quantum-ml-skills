---
name: qml-cross-framework-benchmarking
description: Evaluation skill for fair comparisons across PennyLane plus PyTorch, Qiskit-backed, and native Qiskit ML branches.
category: benchmarking
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
handoff_to: []
---

# qml-cross-framework-benchmarking

## Purpose

Use this skill to design and run fair comparisons across PennyLane + PyTorch, Qiskit-backed execution, and any native Qiskit ML branches. The goal is to make migration and architecture decisions from controlled evidence instead of anecdotal runtime impressions or incomparable notebook results.

## Use this skill when

- Comparing interfaces, optimizers, or backends.
- Reporting results after a migration to cleaner PyTorch training or Qiskit support.
- Validating whether a new framework branch actually improved anything.

## Do not use this skill when

- There is no stable baseline yet.
- The underlying model definition is still changing rapidly.
- The task is simply to implement a model, not compare systems.

## Required inputs

Before applying this skill, identify:

- baseline model and comparison candidates
- dataset split and seed policy
- metrics to report
- backend and shot configuration
- runtime measurement method
- compile-vs-run reporting policy where relevant

## Core rules

1. **Hold the task definition constant.**
2. **Change one major dimension at a time when possible.**
3. **Report backend, interface, optimizer, and shot context with the metrics.**

## Decision rules

### What counts as a fair comparison

- same dataset split
- same metric set
- same preprocessing logic
- same seed policy where practical
- clear runtime accounting rules

### What must be reported

- task metrics
- runtime metrics
- backend/interface metadata
- any known constraint that makes equivalence imperfect

## Implementation guidance

### Recommended migration sequence

1. Freeze the baseline.
2. Define the comparison matrix.
3. Record config and seed rules.
4. Run each branch under the same reporting policy.
5. Summarize results with caveats instead of declaring a winner too early.

### Recommended code-shape pattern

- one shared evaluation harness
- one config schema for compared runs
- one reporting table that includes model and execution metadata

## Pitfalls to avoid

- comparing notebook outputs with different hidden states
- changing batch size, optimizer, and backend simultaneously
- reporting only final accuracy
- ignoring shot cost, runtime context, or simulator/backend differences in reported results

## Verification checklist

- baseline and candidates are clearly defined
- metrics and runtime rules are matched
- config and seeds are recorded
- backend/interface metadata is preserved in the results
- conclusions are tied to controlled evidence, not impressions

## Output standard

When this skill is applied, benchmark results should be credible enough to support architecture decisions and research notes.
