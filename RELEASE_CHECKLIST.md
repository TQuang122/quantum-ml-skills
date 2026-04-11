# Release Checklist

Use this checklist before publishing a public release of the Quantum ML Skills repository.

## 1. Source library sanity

- [ ] `skills/qml/` is still the source-of-truth
- [ ] all 9 skill directories still contain `SKILL.md`
- [ ] frontmatter exists and is consistent in every `SKILL.md`
- [ ] `depends_on` and `handoff_to` metadata still reflect current routing logic
- [ ] `REQUEST_PATTERNS.md`, `ROUTING.md`, and `STARTER_WORKFLOW.md` are still aligned

## 2. OpenCode workflow sanity

- [ ] `skills/qml/exporters/export_opencode.py` runs successfully
- [ ] `install/install_opencode.py` runs successfully
- [ ] `install/install_opencode.sh` works as a shell wrapper
- [ ] `install/doctor_opencode.py` reports the expected installed structure
- [ ] global installs still target `~/.config/opencode/skills/qml-skills/`
- [ ] global installs do not reset the whole OpenCode skills root

## 3. Validation steps

- [ ] run Python diagnostics on `install/`
- [ ] run Python diagnostics on `skills/qml/exporters/`
- [ ] run exporter dry-run:

```bash
python skills/qml/exporters/export_opencode.py --dry-run
```

- [ ] run installer dry-run:

```bash
bash install/install_opencode.sh --project-root . --dry-run
```

- [ ] run doctor on a known-good local install:

```bash
python install/doctor_opencode.py --path .opencode/skills
```

## 4. GitHub-facing docs

- [ ] root `README.md` still matches actual commands and paths
- [ ] `examples/use-with-opencode.md` still matches current installer behavior
- [ ] `CONTRIBUTING.md` matches the actual source → exporter → docs workflow
- [ ] `CHANGELOG.md` is updated for the release
- [ ] release notes draft exists and is ready to paste into GitHub Releases

## 5. Collaboration scaffolding

- [ ] `.github/ISSUE_TEMPLATE/` is present
- [ ] `.github/PULL_REQUEST_TEMPLATE.md` is present
- [ ] `.github/workflows/validate.yml` matches current Python tool paths

## 6. Release metadata

- [ ] choose version tag (for example `v0.1.0`)
- [ ] update changelog from `Unreleased` into the release section if needed
- [ ] prepare GitHub release title and notes
- [ ] confirm license is present

## 7. Recommended release flow

1. run validation locally
2. review docs and commands one final time
3. create commit for release state
4. tag release (for example `v0.1.0`)
5. publish GitHub release with the prepared release notes
