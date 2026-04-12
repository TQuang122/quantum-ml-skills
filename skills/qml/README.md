# Quantum Machine Learning Skill Library

This folder is a project-local proposal for a QML skill library.

Because the workspace currently has no existing `SKILL.md` files or local skill-directory convention, this proposal uses a neutral project path:

- `skills/qml/`

That keeps the library versioned with the repo, easy to review, and easy to migrate later into another runtime-specific skill location if needed.

## Recommended directory structure

```text
skills/
└── qml/
    ├── README.md
    ├── REQUEST_PATTERNS.md
    ├── EXPORT_STRATEGY.md
    ├── ROUTING.md
    ├── STARTER_WORKFLOW.md
    ├── TEMPLATE.md
    ├── exporters/
    │   ├── README.md
    │   └── export_opencode.py
    ├── evals/
    │   ├── README.md
    │   ├── routing/
    │   │   ├── ambiguous-routing.md
    │   │   ├── debugging-routing.md
    │   │   ├── reproducibility-routing.md
    │   │   └── paper-replication-routing.md
    │   ├── implementation/
    │   │   ├── pennylane-qnn-gold-task.md
    │   │   ├── pytorch-interface-gold-task.md
    │   │   ├── pytorch-training-gold-task.md
    │   │   └── qiskit-backends-gold-task.md
    │   └── research/
    │       ├── benchmarking-gold-task.md
    │       ├── debugging-gold-task.md
    │       ├── paper-replication-gold-task.md
    │       └── reproducibility-gold-task.md
    ├── exports/
    │   └── opencode/
    │       └── README.md
    ├── templates/
    │   ├── README.md
    │   ├── pennylane-qnn/
    │   │   ├── README.md
    │   │   └── src/
    │   │       ├── config.py
    │   │       └── model.py
    │   ├── qml-pytorch-interface/
    │   │   ├── README.md
    │   │   └── src/
    │   │       ├── interface.py
    │   │       └── hybrid_model.py
    │   ├── qml-pytorch-training/
    │   │   ├── README.md
    │   │   └── src/
    │   │       ├── config.py
    │   │       ├── metrics.py
    │   │       └── train.py
    │   └── pennylane-qiskit-backends/
    │       ├── README.md
    │       └── src/
    │           ├── runtime_config.py
    │           └── backends.py
    ├── qml-foundations/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-pytorch-router/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-debugging/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-reproducibility/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-paper-replication/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── pennylane-qnn/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-pytorch-interface/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-pytorch-training/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qml-pytorch-performance-patterns/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── pennylane-qiskit-backends/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    ├── qiskit-machine-learning-interop/
    │   ├── SKILL.md
    │   ├── prompts/
    │   │   └── quickstart.md
    │   └── examples/
    │       └── workflows.md
    └── qml-cross-framework-benchmarking/
        ├── SKILL.md
        ├── prompts/
        │   └── quickstart.md
        └── examples/
            └── workflows.md
```

## Design principles

1. **PennyLane stays the main abstraction layer** for circuits, models, and research workflows.
2. **PyTorch is the primary training/interface layer** for hybrid QML work in this repo.
3. **Qiskit extends the backend and IBM ecosystem path**, not the default authoring model.
4. **Cross-framework benchmarking is first-class** so experiments do not drift into unfair comparisons.
5. Skills should be **modular, composable, and specific** enough for an agent to apply without guessing.

## The 12 recommended skills

### 1. `qml-foundations`
- **Role:** Grounding skill for problem framing in quantum machine learning.
- **Use when:** Starting a new QML task, selecting problem formulations, deciding whether a task is actually a good fit for QML.
- **What it covers:** Task types, simulator vs hardware, variational vs kernel methods, realistic success metrics, and signs that a classical baseline is the better choice.
- **Why it exists:** Prevents shallow “quantum for everything” decisions.

### 2. `qml-pytorch-router`
- **Role:** Meta-skill that routes a PyTorch-first QML request to the right implementation skill.
- **Use when:** You know the project is PennyLane + PyTorch centered but still need to decide whether the task is mainly about model architecture, PyTorch interface cleanup, training-loop structure, or Qiskit backend extension.
- **What it covers:** Intent detection, routing rules, scope boundaries, and handoff guidance for `pennylane-qnn`, `qml-pytorch-interface`, `qml-pytorch-training`, and `pennylane-qiskit-backends`.
- **Why it exists:** It reduces confusion between nearby skills that all operate inside the same hybrid QML stack.

### 3. `qml-debugging`
- **Role:** Diagnostic skill for identifying what is actually broken in a PennyLane + PyTorch QML workflow before choosing the fix path.
- **Use when:** A model fails forward passes, gradients are unusable, training does not learn, outputs have the wrong shape, or backend behavior differs unexpectedly.
- **What it covers:** shape mismatches, output/measurement mismatches, gradient diagnostics, barren plateau indicators, shot-related instability, and backend-specific debugging boundaries.
- **Why it exists:** the library already routes work well, but it needs a dedicated skill for failure analysis rather than only happy-path implementation.

### 4. `qml-reproducibility`
- **Role:** Reproducibility skill for making QML experiments rerunnable, comparable, and defensible across reruns, machines, and backends.
- **Use when:** You need explicit seed control, config capture, backend/shot recording, artifact naming, or run manifests before claiming stable results.
- **What it covers:** deterministic split discipline, seed policy, environment and backend metadata capture, run manifests, and reproducibility hygiene before benchmarking or release.
- **Why it exists:** training and benchmarking already mention reproducibility, but the library needs one dedicated owner for the full reproducibility layer.

### 5. `qml-paper-replication`
- **Role:** Research translation skill for turning QML papers into concrete implementation and evaluation plans.
- **Use when:** You need to extract assumptions from a paper, map the methodology into code modules, reproduce baselines, or decide whether results are replicated versus only approximated.
- **What it covers:** paper-to-code mapping, missing-detail handling, baseline replication, deviation logs, and result-verdict discipline.
- **Why it exists:** the library already builds and benchmarks models well, but it needs a dedicated owner for paper replication workflows.

### 6. `pennylane-qnn`
- **Role:** Core implementation skill for PennyLane-first hybrid models.
- **Use when:** Building or refactoring variational classifiers, data-reuploading models, and hybrid quantum-classical training loops in the current repo.
- **What it covers:** QNode structure, devices, ansatz layout, measurements, PyTorch integration, and clean separation of circuit/training/evaluation logic.
- **Why it exists:** It matches the repo’s current reality: PennyLane + PyTorch + variational classifiers.

### 7. `qml-pytorch-interface`
- **Role:** PyTorch-specific interface skill for PennyLane circuits.
- **Use when:** Converting notebook-style PennyLane experiments into clean PyTorch-compatible model paths with explicit tensors, parameters, and prediction boundaries.
- **What it covers:** tensor handling, QNode integration, parameter management, module boundaries, and migration from ad hoc notebook code to PyTorch-first structure.
- **Why it exists:** the repo already uses PyTorch, so this should be the default training path.

### 8. `qml-pytorch-training`
- **Role:** Standardized training-loop skill for PennyLane + PyTorch.
- **Use when:** Replacing notebook optimizer calls with reusable PyTorch training loops that are easier to benchmark and reproduce.
- **What it covers:** tensor parameters, optimizer selection, batching, logging, validation, reproducibility, and fair comparison against older notebook flows.
- **Why it exists:** PyTorch is already part of the current stack and should be the main training discipline.

### 9. `qml-pytorch-performance-patterns`
- **Role:** Performance engineering skill for PennyLane + PyTorch QML experiments.
- **Use when:** training or inference becomes slow, batching needs cleanup, or simulator-heavy workloads need better throughput discipline.
- **What it covers:** batching strategy, device placement, profiling, DataLoader discipline, simulator/runtime measurement, and safe performance claims.
- **Why it exists:** PyTorch-first projects still need performance rigor, especially when hybrid models grow beyond toy notebooks.

### 10. `pennylane-qiskit-backends`
- **Role:** Backend-extension skill for running PennyLane workflows on Qiskit simulators and IBM-compatible paths.
- **Use when:** Keeping PennyLane circuits while adding Qiskit execution backends, shot-based evaluation, or IBM backend support.
- **What it covers:** Plugin boundaries, backend selection, simulator vs remote tradeoffs, shot configuration, and interoperability caveats.
- **Why it exists:** This is the safest way to add Qiskit without splitting the codebase into parallel frameworks.

### 11. `qiskit-machine-learning-interop`
- **Role:** Specialized interop skill for cases where native Qiskit Machine Learning components are genuinely needed.
- **Use when:** Exploring `EstimatorQNN`, `SamplerQNN`, or `TorchConnector`, and comparing them against PennyLane-based approaches.
- **What it covers:** Scope boundaries, when native Qiskit ML is justified, and how to keep experiments comparable.
- **Why it exists:** Qiskit ML is powerful, but should be a deliberate branch, not the new default path.

### 12. `qml-cross-framework-benchmarking`
- **Role:** Evaluation skill for fair comparisons across PennyLane+PyTorch, Qiskit-backed runs, and any native Qiskit ML branches.
- **Use when:** Reporting results, validating migration decisions, or comparing interfaces/backends.
- **What it covers:** Metric parity, seed control, backend metadata, shot accounting, runtime accounting, and baseline discipline.
- **Why it exists:** Without this, “improvements” are often measurement artifacts.

## Recommended adoption order

1. `qml-foundations`
2. `qml-pytorch-router`
3. `qml-debugging`
4. `qml-reproducibility`
5. `qml-paper-replication`
6. `pennylane-qnn`
7. `qml-pytorch-interface`
8. `qml-pytorch-training`
9. `qml-pytorch-performance-patterns`
10. `pennylane-qiskit-backends`
11. `qml-cross-framework-benchmarking`
12. `qiskit-machine-learning-interop`

## Drafts included now

This proposal now includes a complete first-pass `SKILL.md` for all 12 skills in the library.

## Standardized per-skill template

All skill directories should follow the same structure:

- `SKILL.md` — the durable operational guidance
- `prompts/quickstart.md` — copy-paste prompts for fast use
- `examples/workflows.md` — realistic use patterns and expected outcomes

The common `SKILL.md` section order is:

1. Purpose
2. Use this skill when
3. Do not use this skill when
4. Required inputs
5. Core rules
6. Decision rules
7. Implementation guidance
8. Pitfalls to avoid
9. Verification checklist
10. Output standard

That template is stored in `skills/qml/TEMPLATE.md` so new skills can be added without drifting in style.

## Library-level navigation docs

- `REQUEST_PATTERNS.md` — fast mapping from common user phrases to the right skill or router
- `EXPORT_STRATEGY.md` — source-of-truth, metadata schema, and planned platform export strategy
- `ROUTING.md` — shared routing guide for deciding which implementation skill should own a request
- `STARTER_WORKFLOW.md` — practical flow from user request → router → selected skill → execution plan

## Evals

- `evals/README.md` — overview of the gold-task evaluation suite
- `evals/routing/` — routing gold tasks
- `evals/implementation/` — implementation gold tasks
- `evals/research/` — debugging, reproducibility, replication, and benchmarking gold tasks

## Metadata normalization

Each `SKILL.md` now begins with normalized YAML frontmatter for cross-platform export readiness.

Current source metadata fields:

- `name`
- `description`
- `category`
- `maturity`
- `platforms`
- `depends_on`
- `handoff_to`

These fields are treated as source metadata and can be translated later into OpenCode-, Claude Code-, or Antigravity-specific export formats.

## Exporters and generated outputs

- `exporters/README.md` — overview of export utilities
- `exporters/export_opencode.py` — initial OpenCode exporter scaffold
- `exports/opencode/README.md` — generated-output layout for OpenCode exports

Current OpenCode exporter features:

- export all skills or one selected skill
- install directly into a chosen `.opencode/skills/` directory
- emit a JSON summary report after execution

## Repository-level install entrypoint

At the repository root, the OpenCode installer entrypoint is:

- `install/install_opencode.py`

It delegates to `skills/qml/exporters/export_opencode.py` and installs into either:

- project-local `.opencode/skills/`
- global `~/.config/opencode/skills/`

## Starter code templates

- `templates/README.md` — overview of the starter skeletons
- `templates/pennylane-qnn/` — model-oriented skeleton for variational classifiers
- `templates/qml-pytorch-interface/` — Torch-facing wrapper skeleton around a PennyLane model
- `templates/qml-pytorch-training/` — reusable trainer, metrics, and config skeleton
- `templates/pennylane-qiskit-backends/` — backend-selection and device builder skeleton
