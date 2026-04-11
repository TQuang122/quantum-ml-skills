from __future__ import annotations

import torch


def ensure_2d_inputs(inputs: torch.Tensor) -> torch.Tensor:
    if inputs.ndim == 1:
        return inputs.unsqueeze(0)
    return inputs


def ensure_float_inputs(inputs: torch.Tensor) -> torch.Tensor:
    return inputs.to(dtype=torch.float32)


def normalize_binary_targets(targets: torch.Tensor) -> torch.Tensor:
    return targets.to(dtype=torch.float32).view(-1, 1)
