from .utils import do_print


def test():
    from . import init_once

    print(init_once.var)
    do_print()


if __name__ == "__main__":
    test()
