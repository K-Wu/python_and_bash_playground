# Adapted from https://stackoverflow.com/a/62076913/5555077
import torch
import torch.nn as nn


class ExampleLinear(torch.nn.Module):

    def __init__(self):
        super().__init__()
        # Initialize the weight at 1
        self.weight = torch.nn.Parameter(
            torch.Tensor([1]).float(), requires_grad=True
        )

    def forward(self, x):
        return self.weight * x


def oneline_print(*args):
    reprs = [str(arg).replace("\n", "↵") for arg in args]
    print(*reprs, flush=True)


def forward_pre_hook(m, inputs):
    oneline_print("[Forward Pre Hook]", m)


def forward_hook(m, inputs, outputs):
    oneline_print("[Forward Hook]", m)


def full_backward_hook(m, grad_input, grad_output):
    oneline_print("[Full Backward]", m)


def full_backward_pre_hook(m, grad_output):
    oneline_print("[Full Backward Pre]", m)


nn.modules.module.register_module_forward_pre_hook(forward_pre_hook)
nn.modules.module.register_module_forward_hook(forward_hook)
nn.modules.module.register_module_full_backward_pre_hook(
    full_backward_pre_hook
)
nn.modules.module.register_module_full_backward_hook(full_backward_hook)

model = ExampleLinear()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


def calculate_loss(x: torch.Tensor) -> torch.Tensor:
    y = 2 * x
    y_hat = model(x)
    loss = (y - y_hat) ** 2
    return loss.mean()


# With mulitple batches of size 1
batches = [torch.tensor([4.0]), torch.tensor([2.0])]

optimizer.zero_grad()
for i, batch in enumerate(batches):
    # The loss needs to be scaled, because the mean should be taken across the whole
    # dataset, which requires the loss to be divided by the number of batches.
    loss = calculate_loss(batch) / len(batches)
    loss.backward()
    print(f"Batch size 1 (batch {i}) - grad: {model.weight.grad}")
    print(f"Batch size 1 (batch {i}) - weight: {model.weight}")
    if i % 2 == 1:
        # Updating the model after every batch
        optimizer.step()
        print(f"Batch size 1 (accumulation) - grad: {model.weight.grad}")
        print(f"Batch size 1 (accumulation) - weight: {model.weight}")
        optimizer.zero_grad()
