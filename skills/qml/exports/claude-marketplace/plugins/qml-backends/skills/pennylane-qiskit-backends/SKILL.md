---
name: pennylane-qiskit-backends
description: Backend-extension skill for running PennyLane workflows on Qiskit simulators and IBM-compatible paths.
category: backends
maturity: stable
platforms:
  - opencode
  - claude-code
  - antigravity
depends_on:
  - qml-foundations
  - pennylane-qnn
handoff_to:
  - qml-cross-framework-benchmarking
  - qiskit-machine-learning-interop
---

# pennylane-qiskit-backends

## Purpose

Use this skill when extending a PennyLane-first QML codebase to Qiskit-backed execution without rewriting the project into native Qiskit authoring by default. The goal is to preserve PennyLane as the circuit and experiment layer, while using the PennyLane-Qiskit plugin path to access Qiskit simulators, IBM-oriented backend workflows, and shot-based execution patterns.

This skill is the right default when the project wants “Qiskit support” but does not want to fork into a second independent implementation style.

## Use this skill when

- The project already defines models with PennyLane.
- You want to run the same conceptual circuit on Qiskit-backed execution targets.
- You need IBM ecosystem access or Qiskit simulator behavior.
- You need to compare local PennyLane simulators against Qiskit-backed runs.
- You want backend flexibility without abandoning the current repo structure.

## Do not use this skill when

- The task is purely about PyTorch interface or training-loop migration.
- The task explicitly requires native Qiskit Machine Learning abstractions such as `EstimatorQNN` or `TorchConnector`; use a separate interop skill for that.
- The repo should remain a local-only PennyLane simulator project with no backend diversification.

## Required inputs

Before applying this skill, identify:

- Current PennyLane device and interface
- Whether the target is simulation, remote execution, or hardware-adjacent evaluation
- Desired shot configuration
- Expected measurement outputs
- Required backend metadata to log
- Whether results need to stay numerically comparable to existing `default.qubit` or `lightning` runs

## Core rules

1. **PennyLane remains the authoring layer.**
   - Define circuits in PennyLane.
   - Treat Qiskit as an execution/backend extension.

2. **Do not conflate backend switching with interface switching.**
   - PyTorch is the primary interface concern here.
   - Qiskit is a backend concern in this skill.

3. **Make shot settings explicit.**
   - Never rely on vague defaults when comparing simulators or remote runs.
   - Shot count can materially change behavior and performance.

4. **Expect backend-specific differences.**
   - Noise behavior, transpilation, execution semantics, and differentiation support can differ from local simulators.
   - Do not assume identical results across backends.

5. **Switch one dimension at a time.**
   - If you are introducing Qiskit, avoid simultaneously changing ansatz, optimizer, interface, and dataset split.

## Decision rules

### When to add Qiskit support

- Add Qiskit support when backend diversity or IBM-oriented execution is a real requirement.
- Do not add it just because the ecosystem name is popular.

### How to position Qiskit

- **Default path:** PennyLane + plugin-backed Qiskit execution.
- **Specialized path:** native Qiskit ML only when plugin-backed PennyLane is insufficient for the intended experiment.

### How to compare backends

- Keep the circuit semantics fixed.
- Keep the dataset and metrics fixed.
- Log shots, backend name, runtime context, and any backend-specific constraints.
- Report differences as backend differences, not automatic evidence of a better model.

## Implementation guidance

### Recommended migration sequence

1. Keep the current PennyLane circuit intact.
2. Isolate device construction into a configurable layer.
3. Add a Qiskit-backed device path through the appropriate plugin/device configuration.
4. Run a smoke test on a tiny batch.
5. Validate measurement shape and value range.
6. Add explicit shot configuration.
7. Benchmark against the current local simulator under controlled conditions.

### Recommended code-shape pattern

- `build_device(config)` decides backend selection.
- Circuit definition remains backend-agnostic where possible.
- Training/evaluation code receives a configured QNode rather than hard-coding a specific device inline.
- Benchmarking code records backend metadata alongside task metrics.

### Practical boundaries

- Use plugin-backed Qiskit support for backend extension.
- Do not rewrite everything into native Qiskit circuits unless the task explicitly requires that branch.
- If importing or translating existing Qiskit circuits is necessary, keep the conversion boundary explicit and documented.

## Pitfalls to avoid

- Treating Qiskit adoption as a reason to duplicate the entire model implementation
- Hiding shot count or backend choice in notebook state
- Assuming gradients and measurements behave identically across all backends
- Comparing Qiskit-backed runs to local simulators without controlling for shots, randomness, and runtime conditions
- Making hardware or performance claims from a single uncontrolled comparison

## Verification checklist

- Device/backend selection is configurable instead of hard-coded
- The same conceptual PennyLane circuit can run on the chosen Qiskit-backed path
- Shot count is explicit and logged
- Output shape and metric computation remain valid after the backend switch
- Benchmark results include backend metadata and runtime context
- Claims about differences are phrased cautiously and tied to controlled comparisons
- The codebase remains PennyLane-first rather than splitting into parallel authoring models by accident

## Output standard

When this skill is applied, the result should:

- extend the repo with Qiskit support cleanly
- preserve existing PennyLane patterns where possible
- make backend switching deliberate and testable
- avoid accidental framework fragmentation
