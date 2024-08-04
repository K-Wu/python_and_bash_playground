# Adapted from https://github.com/prigoyal/pytorch_memonger/blob/master/tutorial/Checkpointing_for_PyTorch_models.ipynb

# import the checkpoint API
from torch.utils.checkpoint import checkpoint_sequential
import torch.nn as nn
import torch
import traceback


def oneline_print(*args):
    reprs = [str(arg).replace("\n", "↵") for arg in args]
    print(*reprs, flush=True)


def forward_pre_hook(m, inputs):
    oneline_print("[Forward Pre Hook]", m)
    oneline_print(*traceback.format_stack())


def forward_hook(m, inputs, outputs):
    oneline_print("[Forward Hook]", m)


def full_backward_hook(m, grad_input, grad_output):
    oneline_print("[Full Backward]", m)


def full_backward_pre_hook(m, grad_output):
    oneline_print("[Full Backward Pre]", m)
    oneline_print(*traceback.format_stack())


def pack_hook(tensor):
    oneline_print("[Pack Hook]", tensor.shape)
    return tensor


def unpack_hook(tensor):
    oneline_print("[Unpack Hook]", tensor.shape)
    return tensor


nn.modules.module.register_module_forward_pre_hook(forward_pre_hook)
nn.modules.module.register_module_forward_hook(forward_hook)
nn.modules.module.register_module_full_backward_pre_hook(
    full_backward_pre_hook
)
nn.modules.module.register_module_full_backward_hook(full_backward_hook)

# create a simple Sequential model
model = nn.Sequential(
    nn.Linear(100, 50),
    nn.ReLU(),
    nn.Linear(50, 20),
    nn.ReLU(),
    nn.Linear(20, 5),
    nn.ReLU(),
)

# create the model inputs
input_var = torch.randn(1, 100, requires_grad=True)

# set the number of checkpoint segments
segments = 2

# get the modules in the model. These modules should be in the order
# the model should be executed
modules = [module for k, module in model._modules.items()]

# now call the checkpoint API and get the output
# out = model(input_var)
out = checkpoint_sequential(modules, segments, input_var)

# run the backwards pass on the model. For backwards pass, for simplicity purpose,
# we won't calculate the loss and rather backprop on out.sum()
with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
    model.zero_grad()
    out.sum().backward()
