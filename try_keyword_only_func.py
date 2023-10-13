from typing import TypedDict, Unpack, Type, TypeVarTuple, Generic


def keyword_only_func(**kwargs):
    print(kwargs)


class ArgumentsExample(TypedDict):
    arg1: str
    arg2: list[int]


def register(cls: Type[TypedDict]):
    # From https://stackoverflow.com/a/39638276
    assert issubclass(cls, TypedDict)


Ts = TypeVarTuple("Ts")


def keyword_only_func_annotated(**kwargs: Unpack[ArgumentsExample]):
    print(kwargs)


if __name__ == "__main__":
    keyword_only_func(a=1, b=2)

    a: ArgumentsExample = {"arg1": "a", "arg2": [1, 2, 3]}
    register(ArgumentsExample)
    keyword_only_func_annotated(**a)
