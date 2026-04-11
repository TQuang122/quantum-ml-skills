from __future__ import annotations

import torch
from torch import nn

from .interface import ensure_2d_inputs, ensure_float_inputs


class VariationalClassifier(nn.Module):
    def __init__(self, qnode, initial_weights: torch.Tensor, num_outputs: int) -> None:
        super().__init__()
        self.qnode = qnode
        self.weights = nn.Parameter(initial_weights.clone().detach())
        self.num_outputs = num_outputs

    def forward(self, batch_inputs: torch.Tensor) -> torch.Tensor:
        batch_inputs = ensure_float_inputs(ensure_2d_inputs(batch_inputs))
        outputs: list[torch.Tensor] = []
        for sample in batch_inputs:
            result = self.qnode(sample, self.weights)
            result_tensor = (
                torch.stack(list(result))
                if isinstance(result, (list, tuple))
                else torch.atleast_1d(result)
            )
            outputs.append(result_tensor[: self.num_outputs])
        return torch.stack(outputs)
