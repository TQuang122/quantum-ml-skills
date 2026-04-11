from __future__ import annotations

import pennylane as qml

from .runtime_config import BackendConfig


SUPPORTED_BACKENDS: dict[str, str] = {
    "default.qubit": "Local PennyLane simulator",
    "lightning.qubit": "Faster PennyLane simulator",
    "qiskit.aer": "Qiskit-backed simulator via PennyLane plugin",
    "qiskit.remote": "Remote/IBM-oriented execution via PennyLane plugin",
}


def describe_backend(device_name: str) -> str:
    return SUPPORTED_BACKENDS.get(device_name, "Custom backend")


def build_device(config: BackendConfig) -> qml.devices.Device:
    kwargs: dict[str, object] = {"wires": config.wires}

    if config.shots is not None:
        kwargs["shots"] = config.shots

    if (
        config.device_name in {"qiskit.aer", "qiskit.remote"}
        and config.backend_name is not None
    ):
        kwargs["backend"] = config.backend_name

    if config.device_name == "qiskit.remote" and config.provider is not None:
        kwargs["provider"] = config.provider

    return qml.device(config.device_name, **kwargs)
