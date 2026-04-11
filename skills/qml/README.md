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

## The 9 recommended skills

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

### 3. `pennylane-qnn`
- **Role:** Core implementation skill for PennyLane-first hybrid models.
- **Use when:** Building or refactoring variational classifiers, data-reuploading models, and hybrid quantum-classical training loops in the current repo.
- **What it covers:** QNode structure, devices, ansatz layout, measurements, PyTorch integration, and clean separation of circuit/training/evaluation logic.
- **Why it exists:** It matches the repo’s current reality: PennyLane + PyTorch + variational classifiers.

### 4. `qml-pytorch-interface`
- **Role:** PyTorch-specific interface skill for PennyLane circuits.
- **Use when:** Converting notebook-style PennyLane experiments into clean PyTorch-compatible model paths with explicit tensors, parameters, and prediction boundaries.
- **What it covers:** tensor handling, QNode integration, parameter management, module boundaries, and migration from ad hoc notebook code to PyTorch-first structure.
- **Why it exists:** the repo already uses PyTorch, so this should be the default training path.

### 5. `qml-pytorch-training`
- **Role:** Standardized training-loop skill for PennyLane + PyTorch.
- **Use when:** Replacing notebook optimizer calls with reusable PyTorch training loops that are easier to benchmark and reproduce.
- **What it covers:** tensor parameters, optimizer selection, batching, logging, validation, reproducibility, and fair comparison against older notebook flows.
- **Why it exists:** PyTorch is already part of the current stack and should be the main training discipline.

### 6. `qml-pytorch-performance-patterns`
- **Role:** Performance engineering skill for PennyLane + PyTorch QML experiments.
- **Use when:** training or inference becomes slow, batching needs cleanup, or simulator-heavy workloads need better throughput discipline.
- **What it covers:** batching strategy, device placement, profiling, DataLoader discipline, simulator/runtime measurement, and safe performance claims.
- **Why it exists:** PyTorch-first projects still need performance rigor, especially when hybrid models grow beyond toy notebooks.

### 7. `pennylane-qiskit-backends`
- **Role:** Backend-extension skill for running PennyLane workflows on Qiskit simulators and IBM-compatible paths.
- **Use when:** Keeping PennyLane circuits while adding Qiskit execution backends, shot-based evaluation, or IBM backend support.
- **What it covers:** Plugin boundaries, backend selection, simulator vs remote tradeoffs, shot configuration, and interoperability caveats.
- **Why it exists:** This is the safest way to add Qiskit without splitting the codebase into parallel frameworks.

### 8. `qiskit-machine-learning-interop`
- **Role:** Specialized interop skill for cases where native Qiskit Machine Learning components are genuinely needed.
- **Use when:** Exploring `EstimatorQNN`, `SamplerQNN`, or `TorchConnector`, and comparing them against PennyLane-based approaches.
- **What it covers:** Scope boundaries, when native Qiskit ML is justified, and how to keep experiments comparable.
- **Why it exists:** Qiskit ML is powerful, but should be a deliberate branch, not the new default path.

### 9. `qml-cross-framework-benchmarking`
- **Role:** Evaluation skill for fair comparisons across PennyLane+PyTorch, Qiskit-backed runs, and any native Qiskit ML branches.
- **Use when:** Reporting results, validating migration decisions, or comparing interfaces/backends.
- **What it covers:** Metric parity, seed control, backend metadata, shot accounting, runtime accounting, and baseline discipline.
- **Why it exists:** Without this, “improvements” are often measurement artifacts.

## Recommended adoption order

1. `qml-foundations`
2. `qml-pytorch-router`
3. `pennylane-qnn`
4. `qml-pytorch-interface`
5. `qml-pytorch-training`
6. `qml-pytorch-performance-patterns`
7. `pennylane-qiskit-backends`
8. `qml-cross-framework-benchmarking`
9. `qiskit-machine-learning-interop`

## Drafts included now

This proposal now includes a complete first-pass `SKILL.md` for all 9 skills in the library.

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
