# Adapted from https://bo-10000.tistory.com/181
import torch
import torch.nn as nn


class PassThrough1(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        return x

    @staticmethod
    def backward(ctx, grad_output):
        print("Passing through 1!")
        return grad_output


class PassThrough2(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        return x

    @staticmethod
    def backward(ctx, grad_output):
        print("Passing through 2!")
        return grad_output


layer1 = nn.Linear(10, 10)
layer2 = nn.Linear(10, 10)

x = torch.randn(1, 10)
out1 = PassThrough1.apply(layer1(x))
out1_detached = out1.detach()
out1_detached.requires_grad = True
out1_detached.retain_grad()
out2 = PassThrough2.apply(layer2(out1_detached))

out2.mean().backward()
out1.backward(out1_detached.grad)
