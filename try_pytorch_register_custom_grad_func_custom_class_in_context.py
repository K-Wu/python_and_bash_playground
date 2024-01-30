import torch
import math
import csv


class MyMatmul(torch.autograd.Function):
    @staticmethod
    def _forward(ctx, input, weight):
        ctx.save_for_backward(input, weight)
        ctx.csv_writer = csv.reader(
            open("/home/kwu/Downloads/cicc.symobls", "r")
        )
        ctx.self_function = MyMatmul
        return input.mm(weight)

    @staticmethod
    def forward(ctx, input, weight):
        return MyMatmul._forward(ctx, input, weight)

    @staticmethod
    def _backward(ctx, grad_output):
        print("ctx.csv_writer", ctx.csv_writer)
        print("ctx.self_function", ctx.self_function)
        input, weight = ctx.saved_tensors
        grad_input = grad_weight = None
        if ctx.needs_input_grad[0]:
            grad_input = grad_output.mm(weight.t())
            # grad_input = torch.zeros_like(grad_input)
        if ctx.needs_input_grad[1]:
            grad_weight = input.t().mm(grad_output)
            # grad_weight = torch.zeros_like(grad_weight)

        return grad_input, grad_weight

    @staticmethod
    def backward(ctx, grad_output):
        return MyMatmul._backward(ctx, grad_output)


if __name__ == "__main__":
    dtype = torch.float
    device = torch.device("cpu")
    # device = torch.device("cuda:0")  # Uncomment this to run on GPU

    # Create random Tensors for weights. For this example, we need
    # 4 weights: y = a + b * P3(c + d * x), these weights need to be initialized
    # not too far from the correct result to ensure convergence.
    # Setting requires_grad=True indicates that we want to compute gradients with
    # respect to these Tensors during the backward pass.
    input = torch.randn(20, 10, dtype=dtype, device=device, requires_grad=True)
    # input_copy = input.clone()
    # input_copy.detach()
    # input_copy.requires_grad = True
    weight = torch.randn(
        10, 20, dtype=dtype, device=device, requires_grad=True
    )
    # weight_copy = weight.clone()
    # weight_copy.detach()
    # weight_copy.requires_grad = True

    learning_rate = 1e-6
    for t in range(2000):
        # To apply our Function, we use Function.apply method. We alias this as 'P3'.
        my_matmul = MyMatmul.apply

        # Forward pass: compute predicted y using operations; we compute
        # my_matmul(input, weight) and not MyMatmul(input, weight) because
        # the apply method is static
        output = my_matmul(input, weight)
        # output_ref = input_copy.mm(weight_copy)

        # Compute and print loss
        truth_value = torch.randn(20, 20, dtype=dtype, device=device)
        # truth_value_copy = truth_value.clone()
        # truth_value_copy.detach()
        # truth_value_copy.requires_grad = True
        loss = (output - truth_value).pow(2).sum()
        # loss_ref = (output_ref - truth_value_copy).pow(2).sum()
        if t % 100 == 99:
            print(t, loss.item())
            # print(t, loss_ref.item())

        # Use autograd to compute the backward pass.
        loss.backward()

        # Update weights using gradient descent
        with torch.no_grad():
            input -= learning_rate * input.grad
            weight -= learning_rate * weight.grad
            if t % 100 == 99:
                print(
                    "input.grad",
                    input.grad,
                    "weight.grad",
                    weight.grad,
                )

            # Manually zero the gradients after updating weights
            input.grad.zero_()
            weight.grad.zero_()

            # input_copy -= learning_rate * input_copy.grad
            # weight_copy -= learning_rate * weight_copy.grad

            # Manually zero the gradients after updating weights
            # input_copy.grad.zero_()
            # weight_copy.grad.zero_()

    # assert torch.allclose(input, input_copy)
    # assert torch.allclose(weight, weight_copy)
