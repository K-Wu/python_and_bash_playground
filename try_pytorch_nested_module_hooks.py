# Adapted from https://pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html
# Reference: https://pytorch.org/docs/stable/notes/modules.html

import torch.nn as nn
import torch


class MultiplyModule(nn.Module):
    def forward(self, x, y):
        return x * y


def oneline_print(m: ...):
    repr = str(m)
    repr = repr.replace("\n", "↵")
    print(repr)


def forward_pre_hook(m, inputs):
    oneline_print(m)


def forward_hook(m, inputs, outputs):
    oneline_print(m)


nn.modules.module.register_module_forward_pre_hook(forward_pre_hook)
nn.modules.module.register_module_forward_hook(forward_hook)

model = nn.Sequential(
    nn.Linear(10, 100),
    nn.Linear(100, 10),
)

x = torch.randn(10, 10)
loss = model(x).sum()
loss.backward()

model2 = MultiplyModule()
x2 = torch.randn(10, 10)
x2.requires_grad = True
loss2 = model2(x2, x2).sum()
loss2.backward()
