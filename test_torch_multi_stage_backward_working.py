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
out1 = layer1(x)
out1_annotated = PassThrough1.apply(out1)
out1_annotated.retain_grad()
out2 = layer2(out1_annotated)
out2_annotated = PassThrough2.apply(out2)

loss = out2_annotated.mean()
# calculate the gradient of layer 2's parameters
torch.autograd.grad(
    loss, list(layer2.parameters()) + [out1_annotated], retain_graph=True
)
# calculate the gradient of layer 1's parameters
# print(out1_annotated.grad)
torch.autograd.grad(out1_annotated, layer1.parameters(), out1_annotated.grad)
