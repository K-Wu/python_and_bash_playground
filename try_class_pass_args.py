class PassArgs:
    def __init__(self):
        ...

    def print_args(self, *args, **kwargs):
        print(args)
        print(kwargs)


if __name__ == "__main__":
    pa = PassArgs()
    pa.print_args(1, 2, 3, a=4, b=5)
    pa.print_args(4, 2, 3, a=4, b=5)
