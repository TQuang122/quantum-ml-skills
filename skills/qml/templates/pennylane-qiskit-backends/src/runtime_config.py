from dataclasses import dataclass


@dataclass(slots=True)
class BackendConfig:
    device_name: str = "default.qubit"
    wires: int = 4
    shots: int | None = None
    backend_name: str | None = None
    provider: object | None = None
