#!/usr/bin/env python3
# from https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_custom_function.html
# and from https://discuss.pytorch.org/t/ctx-fields-of-functions-non-being-deleted-during-backward/8293

import torch
import math
from torch.utils.checkpoint import (
    detach_variable,
    _supports_autocast,
    _get_device_module,
    _infer_device_type,
    _get_autocast_kwargs,
)

import contextlib


class LegendrePolynomial3(torch.autograd.Function):
    """
    We can implement our own custom autograd Functions by subclassing
    torch.autograd.Function and implementing the forward and backward passes
    which operate on Tensorssave
    """

    @staticmethod
    def forward(ctx, inputs, dummy_kwargs_1=15, dummy_kwargs_2=False):
        """
        In the forward pass we receive a Tensor containing the input and return
        a Tensor containing the output. ctx is a context object that can be used
        to stash information for backward computation. You can cache arbitrary
        objects for use in the backward pass using the ctx.save_for_backward method.
        """
        inputs_to_save = torch.zeros_like(inputs)
        inputs_to_save[:] = inputs
        ctx.save_for_backward(inputs_to_save)

        return 0.5 * (5 * inputs**3 - 3 * inputs)

    @staticmethod
    def backward(ctx, grad_output):
        """
        In the backward pass we receive a Tensor containing the gradient of the loss
        with respect to the output, and we need to compute the gradient of the loss
        with respect to the input.
        """
        (inputs,) = ctx.saved_tensors
        return grad_output * 1.5 * (5 * inputs**2 - 1), None


class FuncWrapper(torch.autograd.Function):
    # Adapted from https://github.com/pytorch/pytorch/blob/f5331aade57725b03c36d5cc6c683f6a6bc0692d/torch/utils/checkpoint.py#L226
    @staticmethod
    def forward(ctx, run_function, *args, **kwargs):
        if len(kwargs) > 0:
            raise ValueError(
                "kwargs not supported. Check https://github.com/pytorch/pytorch/issues/16940"
            )
        ctx.run_function = run_function

        # Save non-tensor inputs in ctx, keep a placeholder None for tensors
        # to be filled out during the backward.
        ctx.inputs = []
        ctx.tensor_indices = []
        tensor_inputs = []
        for i, arg in enumerate(args):
            # print(i, arg, type(arg), torch.is_tensor(arg))
            if torch.is_tensor(arg):
                tensor_inputs.append(arg)
                ctx.tensor_indices.append(i)
                ctx.inputs.append(None)
            else:
                ctx.inputs.append(arg)
        ctx.save_for_backward(*tensor_inputs)
        ctx.kwargs = kwargs

        ctx.device = _infer_device_type(*args)
        ctx.device_autocast_kwargs, ctx.cpu_autocast_kwargs = (
            _get_autocast_kwargs(ctx.device)
        )

        with torch.no_grad():
            outputs = run_function(*args)
        return outputs

    @staticmethod
    def backward(ctx, *args):
        # Copy the list to avoid modifying original list.
        inputs = list(ctx.inputs)
        tensor_indices = ctx.tensor_indices
        tensors = ctx.saved_tensors

        # print(inputs, tensor_indices, tensors)

        # Fill in inputs with appropriate saved tensors.
        for i, idx in enumerate(tensor_indices):
            inputs[idx] = tensors[i]

        # Fill in inputs with appropriate saved tensors.
        for i, idx in enumerate(tensor_indices):
            inputs[idx] = tensors[i]

        detached_inputs = detach_variable(tuple(inputs))

        device_module = _get_device_module(ctx.device)
        device_autocast_ctx = (
            device_module.amp.autocast(**ctx.device_autocast_kwargs)
            if _supports_autocast(ctx.device)
            else contextlib.nullcontext()
        )
        with torch.enable_grad(), device_autocast_ctx, torch.cpu.amp.autocast(
            **ctx.cpu_autocast_kwargs
        ):
            # with torch.enable_grad():
            outputs = ctx.run_function(*detached_inputs, **ctx.kwargs)

        if isinstance(outputs, torch.Tensor):
            outputs = (outputs,)

        # run backward() with only tensor that requires grad
        outputs_with_grad = []
        args_with_grad = []
        for i in range(len(outputs)):
            if torch.is_tensor(outputs[i]) and outputs[i].requires_grad:
                outputs_with_grad.append(outputs[i])
                args_with_grad.append(args[i])
        torch.autograd.backward(outputs_with_grad, args_with_grad)
        # print(outputs, outputs_with_grad, args_with_grad)
        grads = tuple(
            inp.grad if isinstance(inp, torch.Tensor) else None
            for inp in detached_inputs
        )

        # None for run_function
        # print(grads)
        return (None,) + grads


dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0")  # Uncomment this to run on GPU

# Create Tensors to hold input and outputs.
# By default, requires_grad=False, which indicates that we do not need to
# compute gradients with respect to these Tensors during the backward pass.
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

# Create random Tensors for weights. For this example, we need
# 4 weights: y = a + b * P3(c + d * x), these weights need to be initialized
# not too far from the correct result to ensure convergence.
# Setting requires_grad=True indicates that we want to compute gradients with
# respect to these Tensors during the backward pass.
a = torch.full((), 0.0, device=device, dtype=dtype, requires_grad=True)
b = torch.full((), -1.0, device=device, dtype=dtype, requires_grad=True)
c = torch.full((), 0.0, device=device, dtype=dtype, requires_grad=True)
d = torch.full((), 0.3, device=device, dtype=dtype, requires_grad=True)

learning_rate = 5e-6
for t in range(2000):
    # To apply our Function, we use Function.apply method. We alias this as 'P3'.
    P3 = LegendrePolynomial3.apply

    # Forward pass: compute predicted y using operations; we compute
    # P3 using our custom autograd operation.
    y_pred = a + b * FuncWrapper.apply(P3, c + d * x)

    # Do it again to see if Function instances are with different ids
    y_pred = a + b * FuncWrapper.apply(P3, c + d * y_pred)

    # Compute and print loss
    loss = (y_pred - y).pow(2).sum()
    if t % 100 == 99:
        print("t", t, "loss", loss.item())

    # Use autograd to compute the backward pass.
    loss.backward()

    # Update weights using gradient descent
    with torch.no_grad():
        a -= learning_rate * a.grad
        b -= learning_rate * b.grad
        c -= learning_rate * c.grad
        d -= learning_rate * d.grad

        # Manually zero the gradients after updating weights
        a.grad = None
        b.grad = None
        c.grad = None
        d.grad = None

print(f"Result: y = {a.item()} + {b.item()} * P3({c.item()} + {d.item()} x)")
