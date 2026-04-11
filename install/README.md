# Installers

This directory contains end-user installation entrypoints for supported platforms.

## Current installer

- `install_opencode.sh` — shell wrapper that delegates to the Python installer so users do not need to call Python directly
- `install_opencode.py` — installs exported skills into a project-local or global OpenCode skills directory
- `doctor_opencode.py` — inspects an OpenCode skills directory and reports installed skill structure

Global installs now default to a namespaced path:

- `~/.config/opencode/skills/qml-skills/`

This avoids resetting the global OpenCode skills root directly.

## Examples

```bash
bash install/install_opencode.sh --project-root .
bash install/install_opencode.sh --project-root . --skill qml-pytorch-training
bash install/install_opencode.sh --global
bash install/install_opencode.sh --project-root . --dry-run
python install/install_opencode.py --project-root .
python install/install_opencode.py --project-root . --skill qml-pytorch-training
python install/install_opencode.py --global
python install/install_opencode.py --project-root . --dry-run
python install/install_opencode.py --global --dry-run
python install/doctor_opencode.py --path .opencode/skills
python install/doctor_opencode.py --path ~/.config/opencode/skills/qml-skills
```

## Manual fallback

If a user does not want to run the installer, they can still export and copy generated skill folders manually. See:

- `examples/use-with-opencode.md`
