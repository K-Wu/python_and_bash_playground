# From https://github.com/elliotwaite/pytorch-hooks-tutorial/blob/master/2_module_forward_hooks/3_module_with_hooks_and_prints.py
import torch
import torch.nn as nn


class LegendrePolynomial3(torch.autograd.Function):
    # Adapted from https://pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html
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
        ctx.save_for_backward(inputs)
        # These stored as attributes without using save_for_backward will not trigger
        # pack / unpack hooks
        ctx.dummy = dummy_kwargs_1
        ctx.dummy2 = dummy_kwargs_2

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


class SumNet(nn.Module):
    def __init__(self):
        super(SumNet, self).__init__()

    @staticmethod
    def forward(a, b, c, d):
        d = a + b + c + d

        print("forward():")
        print("    a:", a)
        print("    b:", b)
        print("    c:", c)
        print()
        print("    d:", d)
        print()

        return d


from weakref import WeakKeyDictionary
from collections import defaultdict
from uuid import uuid4


class UniqueIdMap(WeakKeyDictionary):
    def __init__(self, dict=None):
        super().__init__(self)
        # replace data with a defaultdict to generate uuids
        self.data = defaultdict(uuid4)
        if dict is not None:
            self.update(dict)


uniqueidmap = UniqueIdMap()

# Adapted from https://stackoverflow.com/questions/52096582/how-unique-is-pythons-id


def uniqueid(obj):
    """Produce a unique integer id for the object.

    Object must me *hashable*. Id is a UUID and should be unique
    across Python invocations.

    """
    return uniqueidmap[obj].int


def pack_hook(tensor):
    # Check if a and d share the same uniqueid
    print(f"Dummy pack hook for {uniqueid(tensor)} {id(tensor)}.")

    return tensor


def unpack_hook(tensor):
    # Check if a and d share the same uniqueid
    print(f"Dummy pack hook for {uniqueid(tensor)} {id(tensor)}.")
    return tensor


def main():
    sum_net = SumNet()

    a = torch.tensor(1.0, requires_grad=True)
    b = torch.tensor(2.0, requires_grad=True)
    c = torch.tensor(3.0, requires_grad=True)
    aa = a

    print("start")
    print()
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print()
    print("before model")
    print()

    with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
        d = sum_net(
            LegendrePolynomial3.apply(a),
            b,
            c=c,
            d=LegendrePolynomial3.apply(aa),
        )
        d.backward()

    print("after model")
    print()
    print("d:", d)


if __name__ == "__main__":
    main()
