---
name: qml-pytorch-performance-patterns
description: Performance optimization skill for PennyLane plus PyTorch QML workloads.
category: performance
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - qml-pytorch-training
handoff_to:
  - qml-cross-framework-benchmarking
---

# qml-pytorch-performance-patterns

## Purpose

Use this skill to optimize the runtime characteristics of PennyLane + PyTorch QML experiments after correctness is already established. The goal is to improve throughput and measurement quality through better batching, device placement, profiling, and simulator-aware performance discipline rather than through uncontrolled micro-optimizations.

## Use this skill when

- PennyLane + PyTorch code is correct but slow.
- Batch inference or training throughput is poor.
- You need clearer measurement of simulator cost versus training-loop overhead.
- You want to compare performance changes without breaking correctness.

## Do not use this skill when

- The model is still failing forward or loss checks.
- The main task is optimizer design or backend switching.
- There is no stable baseline to profile against.

## Required inputs

Before applying this skill, identify:

- current runtime bottleneck hypothesis
- batch sizes and dataset sizes
- device placement assumptions
- simulator/backend choice
- current measurement method
- baseline implementation for comparison

## Core rules

1. **Correctness before speed.**
2. **Profile before rewriting.**
3. **Separate model, simulator, and training-loop costs when reporting results.**

## Decision rules

### When to optimize batching

- Optimize batching first when repeated single-sample execution dominates runtime.
- Keep batch semantics stable when comparing before/after performance.

### When to optimize device placement

- Move tensors and model state deliberately.
- Avoid accidental host/device churn in tight loops.

### When to stop optimizing

- Stop when the next optimization would compromise clarity or measurement fairness more than it helps throughput.

## Implementation guidance

### Recommended migration sequence

1. Measure the current path.
2. Identify whether the bottleneck is batching, preprocessing, simulator calls, or logging overhead.
3. Improve one dimension at a time.
4. Re-measure under the same conditions.
5. Keep a readable reference path for sanity checks.

### Recommended code-shape pattern

- one reference implementation
- one profiled performance path
- one small harness for timing and metric collection

## Pitfalls to avoid

- profiling an unstable model
- comparing performance with different batch semantics
- hiding preprocessing changes inside the benchmark
- reporting speedups without identifying what work was actually reduced

## Verification checklist

- baseline timing exists
- bottleneck hypothesis is explicit
- optimized path preserves output correctness
- runtime measurements are collected under matched conditions
- conclusions identify whether gains came from batching, device placement, or reduced overhead

## Output standard

When this skill is applied, performance work should produce credible improvements and not just noisier experiments.
