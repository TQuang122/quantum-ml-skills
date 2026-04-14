---
name: qml-paper-replication
description: Research translation skill for turning QML papers into concrete implementation and evaluation plans.
category: replication
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - qml-reproducibility
handoff_to:
  - pennylane-qnn
  - qml-pytorch-training
  - qml-cross-framework-benchmarking
  - qml-debugging
---

# qml-paper-replication

## Purpose

Use this skill when you need to turn a QML paper into a concrete implementation and evaluation plan. The goal is to extract the paper's assumptions, identify what is explicit versus missing, map methodology into code modules, reproduce the stated baselines, and document whether the outcome is truly replicated, only approximated, or still unresolved.

## Use this skill when

- you want to implement a QML paper faithfully
- you need to extract architecture, optimizer, dataset, and backend assumptions from a paper
- you want to reproduce the baselines or figures from a paper
- you need to decide whether a reported result is replicated versus only approximated
- you need a disciplined deviation log for missing paper details

## Do not use this skill when

- the task is only problem framing without a specific paper target; use `qml-foundations`
- the task is only about making an experiment reproducible after implementation; use `qml-reproducibility`
- the task is only about fair comparison between already implemented branches; use `qml-cross-framework-benchmarking`
- the task is only about debugging a broken implementation; use `qml-debugging`
- the task is only about writing the model code once the paper plan is already fixed; use `pennylane-qnn`

## Required inputs

Before applying this skill, identify:

- the target paper or paper section
- reported task, dataset, and baseline claims
- model architecture and encoding assumptions
- training and optimizer assumptions
- backend, shot, and simulator assumptions
- figures, tables, or metrics that matter for replication

## Core rules

1. **Treat the paper as a specification, not a complete implementation.**
2. **Separate explicit paper facts from assumptions you must infer.**
3. **Replicate baselines before claiming quantum results are reproduced.**
4. **Document every meaningful deviation from the paper.**

## Decision rules

### Extracting assumptions

- Capture all explicit hyperparameters, dataset details, backend settings, and evaluation metrics.
- If the paper omits a detail, mark it as an assumption instead of silently inventing it.

### Replication verdicts

- Use `replicated` when the core reported behavior or metrics are matched within reasonable experimental variance.
- Use `approximated` when the same overall trend appears but quantitative agreement is weaker or assumptions had to be filled in.
- Use `unresolved` when key paper details are missing or the implementation cannot support the claim yet.

### Baseline discipline

- Reproduce at least the paper's main classical baseline before claiming meaningful replication of the quantum result.
- If the baseline itself is unclear, flag that before spending effort on the quantum branch.

## Implementation guidance

### Recommended replication sequence

1. Extract paper assumptions and missing details.
2. Map the paper into model, training, dataset, and backend modules.
3. Define the baseline replication plan.
4. Define the quantum implementation plan.
5. Define the comparison and verdict criteria.
6. Record deviations during implementation.

### Recommended paper-to-code outputs

When using this skill, produce:

- extracted paper assumptions
- missing details and chosen assumptions
- module mapping plan
- baseline plan
- quantum plan
- replication verdict criteria
- deviation log template

### Minimum replication artifacts

- assumption table
- baseline definition
- implementation checklist
- deviation log
- verdict summary (`replicated`, `approximated`, or `unresolved`)

## Pitfalls to avoid

- assuming unstated paper details are “standard” without documenting them
- skipping the classical baseline because the quantum path is more interesting
- treating a rough trend match as full replication without qualification
- changing multiple paper assumptions at once and still claiming fidelity
- forgetting to record where your implementation differs from the paper

## Verification checklist

- explicit paper assumptions are extracted
- missing details are marked and resolved visibly
- baseline replication plan exists
- quantum implementation plan exists
- verdict criteria are defined in advance
- deviations are documented instead of hidden

## Output standard

When this skill is applied well, a paper becomes a concrete, auditable implementation plan with a clear replication standard instead of a vague inspiration source.
