from __future__ import annotations

import pennylane as qml
import torch

from .config import QNNConfig


def build_device(config: QNNConfig) -> qml.devices.Device:
    kwargs: dict[str, object] = {"wires": config.wires}
    if config.shots is not None:
        kwargs["shots"] = config.shots
    return qml.device(config.device_name, **kwargs)


def initial_weights(config: QNNConfig) -> torch.Tensor:
    return 0.01 * torch.randn(config.layers, config.wires, 3)


def encode_inputs(inputs: torch.Tensor, wires: range) -> None:
    features = inputs[: len(wires)]
    qml.AngleEmbedding(features, wires=wires, rotation="Y")


def variational_block(weights: torch.Tensor, wires: range) -> None:
    qml.StronglyEntanglingLayers(weights, wires=wires)


def build_qnode(config: QNNConfig):
    wires = range(config.wires)
    device = build_device(config)

    @qml.qnode(device, interface="torch")
    def qnode(inputs: torch.Tensor, weights: torch.Tensor):
        encode_inputs(inputs, wires)
        variational_block(weights, wires)
        return [qml.expval(qml.PauliZ(i)) for i in range(config.output_dim)]

    return qnode


def predict_logits(
    qnode, batch_inputs: torch.Tensor, weights: torch.Tensor
) -> torch.Tensor:
    outputs: list[torch.Tensor] = []
    for sample in batch_inputs:
        result = qnode(sample, weights)
        result_tensor = (
            torch.stack(list(result))
            if isinstance(result, (list, tuple))
            else torch.atleast_1d(result)
        )
        outputs.append(result_tensor)
    return torch.stack(outputs)


if __name__ == "__main__":
    config = QNNConfig()
    qnode = build_qnode(config)
    weights = initial_weights(config)
    dummy_batch = torch.randn(3, config.input_dim)
    logits = predict_logits(qnode, dummy_batch, weights)
    print("Logit shape:", tuple(logits.shape))
