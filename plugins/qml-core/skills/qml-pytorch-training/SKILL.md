---
name: qml-pytorch-training
description: Standardized training-loop skill for PennyLane plus PyTorch experiments.
category: training
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - qml-pytorch-interface
handoff_to:
  - qml-cross-framework-benchmarking
  - qml-pytorch-performance-patterns
---

# qml-pytorch-training

## Purpose

Use this skill when a PennyLane + PyTorch experiment needs a disciplined, reproducible, benchmarkable training loop. The goal is to replace one-off notebook optimizer calls with explicit parameter flow, clear optimizer state, stable batching, and metric logging that supports both practical iteration and fair comparison with other experimental branches.

## Use this skill when

- The QNode path already works and now needs a reusable training loop.
- You want to replace notebook-local optimization code with a clearer PyTorch structure.
- You need clean train/validation accounting.
- You want reproducible experiments for variational classifiers.
- You want fair comparison with older notebook baselines or Qiskit-backed runs.

## Do not use this skill when

- The forward pass is still unstable.
- The main task is backend switching.
- The task is really about interface cleanup rather than training discipline.

## Required inputs

Before applying this skill, identify:

- parameter initialization scheme
- loss function
- metric set
- optimizer candidates
- batch strategy
- seed policy
- runtime and logging expectations

## Core rules

1. **Treat parameters and optimizer state explicitly.**
2. **Keep training logic separate from circuit definition.**
3. **Benchmark fairly against prior baselines.**

## Decision rules

### Optimizer selection

- Start with Adam for most variational-classifier work.
- Use SGD or momentum variants only when the experiment specifically needs optimizer comparisons.
- Add schedulers only when there is a measured benefit or a clear research question.

### Update granularity

- Use full-batch training for very small demonstration datasets when simplicity matters most.
- Use mini-batching when scale or fairness against classical baselines requires it.

### Logging strategy

- Log loss and the main task metric at minimum.
- Also log seed, optimizer config, backend choice, and runtime context.

## Implementation guidance

### Recommended migration sequence

1. Freeze the current forward path.
2. Define a scalar loss function.
3. Build an explicit optimizer setup.
4. Add train and validation steps.
5. Add logging on a fixed schedule.
6. Record enough metadata to reproduce the run.

### Recommended code-shape pattern

- `init_params(...)`
- `predict(...)`
- `loss_fn(...)`
- `train_step(...)`
- `evaluate(...)`
- outer training loop with explicit logging

### Reproducibility guidance

- Make seeds explicit.
- Keep initialization controlled when benchmarking.
- Avoid hidden reshuffling or notebook-state leakage.

## Pitfalls to avoid

- mixing training concerns into the QNode
- benchmarking against old results with different seeds or batch policies
- logging only final accuracy
- changing backend and optimizer in the same comparison without controls

## Verification checklist

- optimizer setup is explicit
- loss path is scalar and stable
- train/validation metrics are logged clearly
- seeds and config are recorded
- results are comparable to the prior PennyLane baseline under matched conditions
- the training loop is understandable enough to move into modules later

## Output standard

When this skill is applied, the result should be a PyTorch-first training workflow that is simple, reproducible, and suitable for fair experimentation.
