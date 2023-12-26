# From https://stackoverflow.com/a/37290710/5555077
class Foo(object):
    def __init__(self):
        print("foo init")
        self.foo_func()

    def foo_func(self):
        print("making bar")
        self.x = Bar()

    def foo_bar_func(self):
        self.x.bar_func()


class Fighters(Foo):
    def __init__(self):
        print("fighters init")
        Foo.__init__(self)

    def func1(self):
        Foo.some_attribute

    def func2(self):
        Foo.someother_func()


class Bar(object):
    def __init__(self):
        print("bar init")

    def bar_func(self):
        # some stuff here
        print("bar bar_func")


class MyFighters(Fighters):
    def foo_func(self):
        print("making mybar")
        self.x = MyBar()


class MyBar(Bar):
    def bar_func(self):
        print("mybar bar_func")


f2 = MyFighters()
f2.foo_bar_func()

# From https://uwpce-pythoncert.github.io/ProgrammingInPython/modules/SubclassingAndInheritance.html#attribute-resolution-order
print(MyFighters.__mro__)
print(MyFighters.mro())

# Output:
# fighters init
# foo init
# making mybar
# bar init
# mybar bar_func
