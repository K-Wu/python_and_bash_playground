def get_func():
    def func():
        print("func")

    return func


if __name__ == "__main__":
    f1 = get_func()
    f2 = get_func()

    print(f1)
    print(f2)
    print(f1 == f2)
    print(f1 is f2)
    print(f1.__closure__)
    print(f2.__closure__)
