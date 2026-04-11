from dataclasses import dataclass


@dataclass(slots=True)
class TrainingConfig:
    epochs: int = 20
    batch_size: int = 16
    learning_rate: float = 1e-3
    weight_decay: float = 0.0
    seed: int = 7
    log_every: int = 1
