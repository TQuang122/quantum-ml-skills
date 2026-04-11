from __future__ import annotations

import torch


def accuracy_from_logits(logits: torch.Tensor, targets: torch.Tensor) -> float:
    if logits.ndim == 2 and logits.shape[1] == 1:
        predictions = (torch.sigmoid(logits) >= 0.5).to(dtype=targets.dtype).view(-1)
    else:
        predictions = torch.argmax(logits, dim=1)
    return (predictions == targets.view(-1)).to(dtype=torch.float32).mean().item()
