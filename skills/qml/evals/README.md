# QML Skill Evals

This directory contains a lightweight gold-task suite for evaluating the QML skill library.

The goal is not to create a heavy benchmark harness immediately, but to define concrete tasks with expected routing, expected output shape, common mistakes, and pass criteria so the library can be tested consistently over time.

## Structure

```text
evals/
  README.md
  routing/
  implementation/
  research/
```

## What a gold task contains

Each gold-task file should define:

- task description
- intended user request or trigger
- expected primary skill
- optional secondary skill
- why that routing is correct
- expected output shape
- common failure modes
- pass criteria

## Categories

### `routing/`

Tests whether ambiguous and overlapping requests go to the correct owner.

### `implementation/`

Tests whether core implementation skills are selected and framed correctly for concrete code tasks.

### `research/`

Tests whether advanced research-oriented workflows—debugging, reproducibility, paper replication, benchmarking—are handled with the right boundaries and evaluation discipline.

## How to use these evals

1. Pick a gold task.
2. Give the task prompt to the skill system or router.
3. Check whether the chosen owner and reasoning match the gold task.
4. Review whether the response shape matches the expected output contract.

## Current goal

The initial eval suite is intentionally lightweight and markdown-first. It exists to validate routing and skill boundaries before investing in heavier automated grading.
