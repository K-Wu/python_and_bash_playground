# Adapted from https://pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html
import torch

import math

storage = []


def pack_hook(x):
    print("Packing", id(x), x)
    storage.append(x)
    return len(storage) - 1


def unpack_hook(i):
    print("Unpacking", i)
    return storage[i]


with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
    a = torch.randn(5, requires_grad=True)
    y = torch.exp(a)
    z = torch.exp(y)
    print(y.grad_fn._saved_result.equal(y))  # True
    print(y.grad_fn._saved_result is y)  # False
    print(storage)
