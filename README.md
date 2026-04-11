# Quantum ML Skills

Reusable Quantum Machine Learning skill library designed for:

- PennyLane-first modeling
- PyTorch-first training and interface workflows
- optional Qiskit backend integration
- OpenCode-first portability, with future Claude Code and Antigravity exports

This repository contains a source-of-truth skill library under `skills/qml/`, plus routing docs, starter templates, and an OpenCode exporter scaffold.

## Who this is for

- QML researchers working with PennyLane and PyTorch
- AI coding-agent users who want reusable QML skills
- OpenCode users who want installable skill packages
- contributors who want a structured, exportable skill library instead of ad hoc prompts

## Highlights

- 9 reusable QML skills with normalized metadata
- PennyLane-first, PyTorch-first architecture
- optional Qiskit backend workflow support
- OpenCode exporter and installer already scaffolded
- request routing, workflow guidance, and starter templates included

## Quick start

### Install into a local project `.opencode/skills/`

```bash
bash install/install_opencode.sh --project-root .
```

The shell installer is the recommended user-facing entrypoint.

Equivalent Python command:

```bash
python install/install_opencode.py --project-root .
```

### Install globally into OpenCode config

```bash
bash install/install_opencode.sh --global
```

Equivalent Python command:

```bash
python install/install_opencode.py --global
```

By default this installs into a namespaced global path:

```text
~/.config/opencode/skills/qml-skills/
```

That avoids resetting the whole global OpenCode skills root.

### Export only one skill into a local project

```bash
bash install/install_opencode.sh --project-root . --skill qml-pytorch-training
```

Equivalent Python command:

```bash
python install/install_opencode.py --project-root . --skill qml-pytorch-training
```

### Dry run the installer without writing files

```bash
bash install/install_opencode.sh --project-root . --dry-run
```

Equivalent Python command:

```bash
python install/install_opencode.py --project-root . --dry-run
```

### Manual fallback without the installer

If you prefer not to call the installer, you can export skills first and copy the generated output manually. See:

- `examples/use-with-opencode.md`

## Repository layout

```text
.
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── install/
│   ├── install_opencode.sh
│   ├── install_opencode.py
│   └── doctor_opencode.py
└── skills/
    └── qml/
        ├── README.md
        ├── REQUEST_PATTERNS.md
        ├── EXPORT_STRATEGY.md
        ├── ROUTING.md
        ├── STARTER_WORKFLOW.md
        ├── TEMPLATE.md
        ├── exporters/
        ├── exports/
        ├── templates/
        └── <skill-directories>/
```

## Skill catalog

Current skills:

- `qml-foundations`
- `qml-pytorch-router`
- `pennylane-qnn`
- `qml-pytorch-interface`
- `qml-pytorch-training`
- `qml-pytorch-performance-patterns`
- `pennylane-qiskit-backends`
- `qiskit-machine-learning-interop`
- `qml-cross-framework-benchmarking`

See:

- `skills/qml/README.md`
- `skills/qml/REQUEST_PATTERNS.md`
- `skills/qml/ROUTING.md`

## Key docs

- `skills/qml/README.md` — full library overview
- `skills/qml/REQUEST_PATTERNS.md` — phrase-to-skill routing shortcuts
- `skills/qml/ROUTING.md` — first-blocking-owner routing logic
- `skills/qml/STARTER_WORKFLOW.md` — request → router → skill → execution plan flow
- `skills/qml/EXPORT_STRATEGY.md` — source-of-truth and multi-platform export plan
- `examples/use-with-opencode.md` — practical OpenCode usage walkthrough

## OpenCode support

The repository already includes:

- normalized `SKILL.md` frontmatter for all skills
- `skills/qml/exporters/export_opencode.py`
- generated-output target under `skills/qml/exports/opencode/`
- shell installer entrypoint under `install/install_opencode.sh`
- installer entrypoint under `install/install_opencode.py`
- install validation via `install/doctor_opencode.py`

Global installs are now safer by default because they target:

- `~/.config/opencode/skills/qml-skills/`

instead of resetting the entire global `skills/` root.

## Repository status

This repository is currently best described as:

- **OpenCode-ready** for initial use
- **Claude Code export-ready** at the metadata/source level
- **Antigravity export-ready** at the metadata/source level

The OpenCode path is implemented first because this workspace already includes `.opencode/` tooling.

## Roadmap

- harden the OpenCode exporter and installer
- add Claude Code exporter
- add Antigravity exporter
- add evaluation tasks and gold routing cases

## Collaboration

This repository now includes GitHub collaboration scaffolding under `.github/`:

- issue templates
- pull request template
- a basic validation workflow for installer/exporter Python scripts

## Release prep

- `RELEASE_CHECKLIST.md` — practical checklist before publishing a release
- `RELEASE_NOTES_v0.1.0.md` — draft notes for the first public release

## License

MIT
