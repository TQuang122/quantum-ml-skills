# qml-reproducibility example workflows

## Example 1 — lock down a training run

- Input: “I can train this classifier, but I need to make the result reproducible across reruns.”
- Skill outcome: defines seeds, split policy, config capture, and artifact naming before the next run.

## Example 2 — prepare fair comparisons

- Input: “I want to compare my local PennyLane run against a Qiskit-backed run without hidden drift.”
- Skill outcome: records backend, shot count, split, config, and metadata so later benchmarking is meaningful.

## Example 3 — diagnose reproducibility drift

- Input: “The same experiment gives different results on another machine.”
- Skill outcome: identifies missing reproducibility inputs and routes to `qml-debugging` only if the issue is no longer a config/environment problem.
