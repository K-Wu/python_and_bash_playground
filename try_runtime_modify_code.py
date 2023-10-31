import inspect


def fetch_func_body_and_modify():
    # Example 1: fetch function body and modify the function as string
    # From https://stackoverflow.com/a/58596238
    def func(var):
        print(var)

    def append_lines_to_func_body(arg, func=func, new_func_lines=[]):
        func_string, call_string = inspect.getsource(func), f"func({arg})"
        # Remove indent from function body
        func_string = "\n".join(line[4:] for line in func_string.split("\n"))

        func_string += (
            ("\n" + "\n".join(new_func_lines)) if new_func_lines else ""
        )

        exec(func_string + ";\n" + call_string)

    append_lines_to_func_body(
        124,
        new_func_lines=[
            "print(f'This code is dynamic! Your input was {arg}')",
            "print('end of function')",
        ],
    )
    # Output:
    # This code is dynamic! Your input was 124
    # end of function
    # 124


def define_func_in_runtime():
    # Example 2: Define new functions in runtime
    # From  https://stackoverflow.com/a/11291851
    assert "a" not in globals()

    exec(
        """def a(x):
    return x+1""",
        globals(),
    )

    # To support print(a(2)), you need to declare global a; in the exec string, or declare global() as the scope of exec. Otherwise you need to use locals().get("a")(2) to call the function.
    # From https://stackoverflow.com/a/45535337  and https://stackoverflow.com/a/35336800
    print(a(2))


def modify_class_func():
    # Example 3: Modify class function by subclassing
    # From https://stackoverflow.com/a/50600307
    class testMOD(object):
        def testFunc(self, variable):
            var = variable
            self.something = var + 12
            print("Original:", self.something)

    class testMODNew(testMOD):
        def testFunc(self, variable):
            var = variable
            self.something = var + 1.2
            print("Alternative3:", self.something)

    mytest3 = testMODNew()
    mytest3.testFunc(10)  # Alternative3: 11.2


if __name__ == "__main__":
    fetch_func_body_and_modify()
    define_func_in_runtime()
    modify_class_func()
