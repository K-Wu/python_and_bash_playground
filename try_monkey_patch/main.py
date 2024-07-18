def _monkey_patch_print():
    global var
    print(var)


if __name__ == "__main__":
    from . import module

    module.print_ = _monkey_patch_print
    module.print_()
