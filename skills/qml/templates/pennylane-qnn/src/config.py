from dataclasses import dataclass


@dataclass(slots=True)
class QNNConfig:
    device_name: str = "default.qubit"
    wires: int = 4
    layers: int = 2
    input_dim: int = 4
    output_dim: int = 2
    shots: int | None = None
