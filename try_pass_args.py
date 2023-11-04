from typing import Any, Callable


def exec_func_with_args(func: Callable, args: dict[str, Any]) -> Any:
    """Execute a function with given arguments."""
    return func(**args)


def print_args(a, b, c, d=False, e=15):
    print(a, b, c, d, e)


if __name__ == "__main__":
    exec_func_with_args(print_args, {"a": 1, "b": 2, "c": 3, "d": True, "e": 4})
    exec_func_with_args(print_args, {"a": 1, "b": 2, "c": 3})
    exec_func_with_args(print_args, {"a": 1, "b": 2, "c": 3, "e": 4})
