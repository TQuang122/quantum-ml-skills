# Changelog

## Unreleased

## v0.1.1

### Changed

- safer global OpenCode install path using `~/.config/opencode/skills/qml-skills/`
- shell installer entrypoint via `install/install_opencode.sh`
- GitHub collaboration scaffolding under `.github/`

### Added

- stronger `doctor_opencode.py` validation for frontmatter, expected skill count, and namespace checks
- `qml-debugging`
- `qml-reproducibility`
- `qml-paper-replication`
- `skills/qml/evals/` with routing, implementation, and research gold tasks

## v0.1.0

### Added

- project-local QML skill library under `skills/qml/`
- 9 QML skills with `SKILL.md`, prompts, and examples
- routing and request-pattern documentation
- starter code templates for core skills
- normalized frontmatter metadata for all skills
- OpenCode exporter scaffold
- OpenCode installer scaffold
- OpenCode shell installer and doctor workflow
- GitHub-ready root docs and repo scaffolding
- public release checklist and first release notes draft
