from __future__ import annotations

import random

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from .config import TrainingConfig
from .metrics import accuracy_from_logits


def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)


def make_dataloader(
    inputs: torch.Tensor, targets: torch.Tensor, batch_size: int, shuffle: bool
) -> DataLoader:
    dataset = TensorDataset(inputs, targets)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)


def make_optimizer(model: nn.Module, config: TrainingConfig) -> torch.optim.Optimizer:
    return torch.optim.Adam(
        model.parameters(), lr=config.learning_rate, weight_decay=config.weight_decay
    )


def compute_loss(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    if logits.ndim == 2 and logits.shape[1] == 1:
        return nn.functional.binary_cross_entropy_with_logits(
            logits.view(-1), targets.to(dtype=torch.float32).view(-1)
        )
    return nn.functional.cross_entropy(logits, targets.view(-1).to(dtype=torch.long))


def train_epoch(
    model: nn.Module, loader: DataLoader, optimizer: torch.optim.Optimizer
) -> tuple[float, float]:
    model.train()
    total_loss = 0.0
    total_accuracy = 0.0
    batches = 0

    for batch_inputs, batch_targets in loader:
        optimizer.zero_grad()
        logits = model(batch_inputs)
        loss = compute_loss(logits, batch_targets)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        total_accuracy += accuracy_from_logits(logits.detach(), batch_targets)
        batches += 1

    return total_loss / max(batches, 1), total_accuracy / max(batches, 1)


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader) -> tuple[float, float]:
    model.eval()
    total_loss = 0.0
    total_accuracy = 0.0
    batches = 0

    for batch_inputs, batch_targets in loader:
        logits = model(batch_inputs)
        loss = compute_loss(logits, batch_targets)

        total_loss += loss.item()
        total_accuracy += accuracy_from_logits(logits, batch_targets)
        batches += 1

    return total_loss / max(batches, 1), total_accuracy / max(batches, 1)


def fit(
    model: nn.Module,
    train_inputs: torch.Tensor,
    train_targets: torch.Tensor,
    valid_inputs: torch.Tensor,
    valid_targets: torch.Tensor,
    config: TrainingConfig,
) -> None:
    set_seed(config.seed)
    train_loader = make_dataloader(
        train_inputs, train_targets, config.batch_size, shuffle=True
    )
    valid_loader = make_dataloader(
        valid_inputs, valid_targets, config.batch_size, shuffle=False
    )
    optimizer = make_optimizer(model, config)

    for epoch in range(1, config.epochs + 1):
        train_loss, train_acc = train_epoch(model, train_loader, optimizer)
        valid_loss, valid_acc = evaluate(model, valid_loader)

        if epoch % config.log_every == 0:
            print(
                f"epoch={epoch} train_loss={train_loss:.4f} train_acc={train_acc:.4f} "
                f"valid_loss={valid_loss:.4f} valid_acc={valid_acc:.4f}"
            )
