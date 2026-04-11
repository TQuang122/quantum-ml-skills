# Using Quantum ML Skills with OpenCode

This guide shows the fastest way to use the QML skill library with OpenCode after cloning the repository.

## 1. Clone the repository

```bash
git clone <your-repo-url> qml-skills
cd qml-skills
```

## 2. Install skills into a local project

If you want the skills available only for one project:

```bash
python install/install_opencode.py --project-root /path/to/your-project
```

This installs skills into:

```text
/path/to/your-project/.opencode/skills/
```

## 3. Install skills globally

If you want the skills available across projects:

```bash
python install/install_opencode.py --global
```

This installs skills into:

```text
~/.config/opencode/skills/
```

## 4. Install only one skill

Example:

```bash
python install/install_opencode.py --project-root /path/to/your-project --skill qml-pytorch-training
```

## 5. Export without installing

If you want to inspect generated output first:

```bash
python skills/qml/exporters/export_opencode.py
```

Output is generated under:

```text
skills/qml/exports/opencode/
```

## 6. What gets exported

For each skill, the current exporter maps:

- source `SKILL.md` → exported `SKILL.md`
- source `prompts/` → exported `references/prompts/`
- source `examples/` → exported `references/examples/`

## 7. Suggested usage flow

1. use `REQUEST_PATTERNS.md` to match the user request quickly
2. use `ROUTING.md` if the task is ambiguous
3. use `qml-pytorch-router` if multiple skills overlap
4. apply the selected skill in your OpenCode workflow

## 8. Good starting skills

If you are new to the library, start with:

- `qml-foundations`
- `qml-pytorch-router`
- `pennylane-qnn`
- `qml-pytorch-training`

## 9. Related docs

- `README.md`
- `skills/qml/README.md`
- `skills/qml/REQUEST_PATTERNS.md`
- `skills/qml/ROUTING.md`
- `skills/qml/STARTER_WORKFLOW.md`
