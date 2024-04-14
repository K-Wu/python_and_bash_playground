def print_(a, *args):
    print(a, *args)


if __name__ == "__main__":
    print_("hello")
    print_("hello", "world")
    print_("hello", "hello", "world")
