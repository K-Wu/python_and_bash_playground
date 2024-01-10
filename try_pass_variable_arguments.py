#!/usr/bin/env python3
def b(*args):
    print(args)


def a(*args):
    b(*args)


def c(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    a(1, 2, 3, 4, 5)
    arg_dict = {"a": 1, "b": 2, "c": 3}
    c(**arg_dict)
