# skill-name

## Purpose

State what the skill is for, what system boundary it owns, and what outcomes it should improve.

## Use this skill when

- List concrete situations where this skill is the right tool.
- Prefer task-focused triggers over broad topic labels.

## Do not use this skill when

- List nearby cases that belong to a different skill.
- Protect boundaries to avoid overlap and confusion.

## Required inputs

Before applying this skill, identify:

- model/task context
- framework/backend/interface constraints
- metric and validation expectations
- any required reproducibility or benchmarking constraints

## Core rules

1. State the architectural invariant this skill must preserve.
2. State the main implementation discipline.
3. State the main evaluation discipline.

## Decision rules

### Rule group A

- Explain how to choose among the main options.

### Rule group B

- Explain what to do when constraints conflict.

## Implementation guidance

### Recommended migration sequence

1. Start from the safest minimal change.
2. Validate correctness before optimization.
3. Add performance or ecosystem integrations only after parity is established.

### Recommended code-shape pattern

- List the preferred separation of responsibilities.

## Pitfalls to avoid

- List failure modes, especially ones that produce misleading results.

## Verification checklist

- List the minimum evidence required to treat the work as complete.

## Output standard

State what a good outcome looks like in practical terms.
