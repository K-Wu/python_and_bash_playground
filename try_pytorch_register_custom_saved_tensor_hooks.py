# Adapted from https://pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html
import torch

import math


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


def pack_hook(x):
    print("Packing", x)
    return x


def unpack_hook(x):
    print("Unpacking", x)
    return x


with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
    a = torch.randn(5, requires_grad=True)
    y = torch.exp(a)
    print(y.grad_fn._saved_result.equal(y))  # True
    print(y.grad_fn._saved_result is y)  # False
    # Check if y.grad_fn._saved_result use the same underlying storage as y
    print(
        y.grad_fn._saved_result.untyped_storage().data_ptr()
        == y.untyped_storage().data_ptr()
    )  # True
    print(
        y.grad_fn._saved_result.untyped_storage().size()
        == y.untyped_storage().size()
    )  # True
    print(y.grad_fn._saved_result.stride() == y.stride())  # True

    # print y memory format
    print(
        y.untyped_storage().data_ptr(),
        y.untyped_storage().size(),
        y.stride(),
        y.untyped_storage().type(),
    )

    # Try bck propogation
    learning_rate = 5e-6
    dtype = torch.float
    device = torch.device("cpu")
    x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
    y = torch.sin(x)
    a = torch.full((), 0.0, device=device, dtype=dtype, requires_grad=True)
    b = torch.full((), -1.0, device=device, dtype=dtype, requires_grad=True)
    c = torch.full((), 0.0, device=device, dtype=dtype, requires_grad=True)
    d = torch.full((), 0.3, device=device, dtype=dtype, requires_grad=True)

    y_pred = a + b * LegendrePolynomial3.apply(c + d * x)

    loss = (y_pred - y).pow(2).sum()
    loss.backward()

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
