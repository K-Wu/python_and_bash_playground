from typing import Union, TypeVar

T = TypeVar("T", int, str)


def add(a: T, b: T) -> T:
    return a + b


def add_simple(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    return a + b


if __name__ == "__main__":
    res = add("5", "3")  # This should pass type check.
    res = add(5, 3)  # This should pass type check.
    res = add(5, "3")  # Type check should complain.
