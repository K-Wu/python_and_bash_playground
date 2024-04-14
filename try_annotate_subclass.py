class StrSubClass(str):
    def __init__(self, value: str):
        super().__init__()
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"StrSubClass({self.value})"


def print_(a: str):
    print(a)


if __name__ == "__main__":
    a = StrSubClass("a")
    print_(a)  # a
    print(a)  # a
    print(repr(a))  # StrSubClass(a)
    print(type(a))  # <class '__main__.StrSubClass'>
