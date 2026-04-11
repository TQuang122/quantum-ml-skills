# Template: pennylane-qiskit-backends

Starter skeleton for configurable PennyLane device selection with Qiskit-backed execution paths.

## Files

- `src/runtime_config.py` — backend configuration model
- `src/backends.py` — backend catalog and device builder

## Use this template when

- the PennyLane model should stay intact
- the main task is adding Qiskit-backed simulators or IBM-oriented backend paths

## Next skill to consult

- `pennylane-qiskit-backends`
- optionally `qml-cross-framework-benchmarking` after the backend switch works
