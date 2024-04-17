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
x.requires_grad = True

loss_fn = torch.nn.MSELoss(reduction="sum")


for idx in range(10):
    out1 = layer1(x)
    out1_annotated = PassThrough1.apply(out1)
    # out1_annotated.retain_grad()
    out2 = layer2(out1_annotated)
    out2_annotated = PassThrough2.apply(out2)

    # loss = out2_annotated.mean()
    loss = loss_fn(out2_annotated, torch.randn(1, 10))

    USE_GRAD = False
    if USE_GRAD:
        # calculate the gradient of layer 2's parameters
        grad_2 = torch.autograd.grad(
            loss,
            list(layer2.parameters()) + [out1_annotated],
            retain_graph=True,
        )
        # calculate the gradient of layer 1's parameters
        grad_1 = torch.autograd.grad(
            out1_annotated,
            list(layer1.parameters()) + [x],
            grad_2[-1],
        )
        with torch.no_grad():
            for idx, param in enumerate(layer2.parameters()):
                param -= 0.01 * grad_2[idx]
            for idx, param in enumerate(layer1.parameters()):
                param -= 0.01 * grad_1[idx]
            x -= 0.01 * grad_1[-1]

    else:
        USE_FULL_AUTOMATIC_BACKWARD = False
        if USE_FULL_AUTOMATIC_BACKWARD:
            loss.backward()
        else:
            layer1.zero_grad()
            layer2.zero_grad()

            for param in layer1.parameters():
                param.retain_grad()
            for param in layer2.parameters():
                param.retain_grad()
            out2_annotated.retain_grad()
            x.retain_grad()
            # calculate the gradient of layer 2's parameters
            torch.autograd.backward(
                loss,
                inputs=list(layer2.parameters()) + [out1_annotated],
                retain_graph=True,
            )
            # calculate the gradient of layer 1's parameters
            torch.autograd.backward(
                out1_annotated,
                inputs=list(layer1.parameters()) + [x],
                grad_tensors=out1_annotated.grad,
            )

        with torch.no_grad():
            for idx, param in enumerate(layer2.parameters()):
                param -= 0.01 * param.grad
            for idx, param in enumerate(layer1.parameters()):
                param -= 0.01 * param.grad
            x -= 0.01 * x.grad
