---
name: qml-reproducibility
description: Reproducibility skill for making PennyLane plus PyTorch QML experiments rerunnable, comparable, and defensible.
category: reproducibility
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
  - qml-debugging
---

# qml-reproducibility

## Purpose

Use this skill when a PennyLane + PyTorch QML workflow needs to produce rerunnable, comparable, and defensible results across reruns, machines, collaborators, or backend changes. The goal is to make experiments reproducible beyond a single notebook session by capturing seeds, data splits, configs, backend and shot settings, environment assumptions, and run metadata in a structured way.

## Use this skill when

- the same experiment must produce consistent results across reruns
- you need explicit seed control and deterministic split discipline
- a benchmark or paper claim needs reproducibility evidence
- backend choice, shot count, or runtime context must be recorded with the result
- you want run manifests, artifact naming, or checkpoint discipline
- collaborators or future-you need to rerun the exact same experiment later

## Do not use this skill when

- the workflow is currently broken and the first need is diagnosis; use `qml-debugging`
- the main task is to design the model itself; use `pennylane-qnn`
- the main task is only to clean the PyTorch boundary; use `qml-pytorch-interface`
- the main task is only to design a training loop; use `qml-pytorch-training`
- the main task is only fair comparison between already reproducible branches; use `qml-cross-framework-benchmarking`

## Required inputs

Before applying this skill, identify:

- seed policy for Python, NumPy, and Torch
- dataset split strategy and split seed
- model/training config fields that affect outcomes
- backend name, device, diff method, and shot configuration
- artifact paths for checkpoints and logs
- environment details that must be recorded for reruns

## Core rules

1. **A result without captured configuration is not reproducible.**
2. **A seeded run without a fixed split is still weak reproducibility.**
3. **Backend, shot count, and environment must be treated as experiment inputs.**
4. **Reproducibility comes before benchmarking claims.**

## Decision rules

### Seed control

- Record all seeds explicitly.
- Use one seed policy across reruns unless the experiment is intentionally a multi-seed study.
- If different libraries own randomness, capture each source explicitly.

### Data split discipline

- Use deterministic train/validation/test splits when making comparisons.
- Do not compare runs produced from different implicit splits.

### Config capture

- Capture the full experiment config, not just learning rate and seed.
- Include ansatz depth, qubit count, optimizer, backend, shot count, and metric set.

### Backend recording

- Always record simulator/backend name, shot count, and any hardware-adjacent assumptions.
- Treat backend changes as reproducibility-relevant changes, not implementation trivia.

## Implementation guidance

### Recommended reproducibility sequence

1. Freeze the dataset split and its seed.
2. Freeze the model and training config into a structured config object or manifest.
3. Record backend/device/shot settings.
4. Use consistent artifact naming for checkpoints and logs.
5. Store enough metadata to rerun or audit the result later.

### Recommended code-shape pattern

- one config object for model + training + backend
- one seed setup function
- one manifest or metadata writer
- one artifact naming convention tied to config and run identity

### Minimum reproducibility artifacts

- config snapshot
- seed values
- backend and shot metadata
- metric outputs
- artifact paths or checkpoint names

## Pitfalls to avoid

- claiming reproducibility with only a single hardcoded seed
- changing data split and model config in the same comparison
- failing to record backend and shot settings
- relying on notebook state instead of explicit manifests
- reporting a result that cannot be recreated from saved metadata

## Verification checklist

- seeds are explicit
- split policy is explicit
- model/training/backend config is recorded
- backend and shot metadata are preserved
- artifacts have stable naming
- another run can reproduce the experimental setup without guessing

## Output standard

When this skill is applied well, a QML experiment should be rerunnable and auditable, not just successful once.
