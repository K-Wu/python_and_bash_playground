from typing import (
    Generic,
    TypeVar,
)


T = TypeVar("T")

class MySet(set[T], Generic[T]):
    """
    Set that records analysis passes and transform passes.
    Example:
    ```
    class Program:
        analysis_passes: MySet[Callable]
        transform_passes: MySet[Callable]

        @transform_passes.register
        def do_something(self):
            ...

        @analysis_passes.register
        def check_something(self):
            ...
    ```
    From https://stackoverflow.com/questions/50372342/class-with-a-registry-of-methods-based-on-decorators
    """

    def register(self, method):
        self.add(method)
        return method


class TestRegister:
    passes = MySet()
    @passes.register
    def test():
        pass
    
if __name__ == "__main__":
    print(TestRegister.passes)
    a = TestRegister()
    b = TestRegister()
    print(a.passes)
    print(b.passes)
        