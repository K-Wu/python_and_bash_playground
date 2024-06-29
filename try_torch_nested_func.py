import torch


class MyLinear(torch.nn.Module):
    def __init__(self):
        super(MyLinear, self).__init__()
        self.layer = torch.nn.Linear(4, 4)

    def forward(self, x):
        def _forward(x):
            return self.layer(x)

        return _forward(x)


model = MyLinear()
# Do simple forward and backward pass
x = torch.randn(4, 4, requires_grad=True)
y = model(x)
y.sum().backward()
