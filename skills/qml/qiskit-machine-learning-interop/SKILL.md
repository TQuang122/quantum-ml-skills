---
name: qiskit-machine-learning-interop
description: Specialized interop skill for deliberate experiments with native Qiskit Machine Learning abstractions.
category: interop
maturity: experimental
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - pennylane-qiskit-backends
handoff_to:
  - qml-cross-framework-benchmarking
---

# qiskit-machine-learning-interop

## Purpose

Use this skill when native Qiskit Machine Learning abstractions need to be evaluated or integrated deliberately alongside a PennyLane-first codebase. The goal is to keep native Qiskit ML as a targeted branch for specific experiments such as `EstimatorQNN`, `SamplerQNN`, or `TorchConnector`, rather than letting it accidentally replace the main project architecture.

## Use this skill when

- You need to test native Qiskit ML components directly.
- You want to compare `TorchConnector` against PennyLane-based PyTorch integration.
- A research question specifically depends on Qiskit ML abstractions.

## Do not use this skill when

- Plugin-backed PennyLane + Qiskit execution is sufficient.
- The project only needs IBM-compatible backend access.
- The task is primarily about PyTorch training cleanup, PennyLane circuit cleanup, or backend-only integration.

## Required inputs

Before applying this skill, identify:

- the exact Qiskit ML abstraction under evaluation
- the reason native Qiskit ML is needed
- the PennyLane baseline to compare against
- framework, backend, and metric constraints

## Core rules

1. **Native Qiskit ML is an explicit branch, not the default path.**
2. **Every native Qiskit ML experiment must have a comparison target.**
3. **Interop boundaries must be visible and documented.**

## Decision rules

### When native Qiskit ML is justified

- Use it when the experiment depends on an abstraction that PennyLane plugin-backed execution does not expose cleanly.
- Do not use it just because Qiskit is now present in the repo.

### How to compare

- Compare against a PennyLane baseline with matched data, metrics, and logging discipline.
- Keep architecture changes minimal so comparisons remain interpretable.

## Implementation guidance

### Recommended migration sequence

1. Define the comparison target.
2. Build a minimal native Qiskit ML branch.
3. Match preprocessing and metric logic.
4. Benchmark under controlled conditions.
5. Decide whether native Qiskit ML adds enough value to keep.

### Recommended code-shape pattern

- keep native Qiskit ML experiments in a clearly marked module or directory
- keep comparison utilities shared where possible
- avoid duplicating unrelated preprocessing or evaluation code

## Pitfalls to avoid

- silently replacing PennyLane-first patterns with Qiskit-first patterns
- comparing different models under different preprocessing pipelines
- keeping a native Qiskit ML branch with no documented justification
- mixing backend and architecture changes in one benchmark

## Verification checklist

- the native Qiskit ML branch exists for a documented reason
- comparison targets are explicit
- metrics and dataset splits are matched
- experiment outputs are comparable to the PennyLane baseline
- the repo’s main architecture remains PennyLane-first unless intentionally changed

## Output standard

When this skill is applied, native Qiskit ML usage should remain a disciplined experimental branch rather than architectural sprawl.
