# Adapted from https://pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html
# Reference: https://pytorch.org/docs/stable/notes/modules.html

import torch.nn as nn
import torch


class MultiplyModule(nn.Module):
    def forward(self, x, y):
        return x * y


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

model = nn.Sequential(
    nn.Linear(10, 100),
    nn.Linear(100, 10),
)

parameters = set(
    [p.data.untyped_storage().data_ptr() for p in model.parameters()]
)


def set_paramters_data_timestamp(pdata):
    pdata.timestamp = 12345
    return pdata


paramter_tensors = [id(p.data) for p in model.parameters()]
paramter_tensors2 = [id(p.data) for p in model.parameters()]
print(paramter_tensors, paramter_tensors2)

set_paramters_timestamp = [
    set_paramters_data_timestamp(p) for p in model.parameters()
]
paramter_timestamps = [p.timestamp for p in model.parameters()]


print(parameters)


def pack_hook(x):
    print("Packing", id(x), x.untyped_storage().data_ptr() in parameters)
    return x


def unpack_hook(x):
    print("Unpacking", id(x))
    return x


with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
    x = torch.randn(10, 10)
    x.requires_grad = True
    loss = model(x).sum()
    loss.backward()

    model2 = MultiplyModule()
    x2 = torch.randn(10, 10)
    x2.requires_grad = True
    loss2 = model2(x2, x2).sum()
    loss2.backward()
