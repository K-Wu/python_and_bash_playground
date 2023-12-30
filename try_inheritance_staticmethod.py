# From https://www.geeksforgeeks.org/method-overriding-in-python/#
# Python program to demonstrate
# method overriding


# Defining parent class
class Parent:
    custom_str = "custom_str"  # class variable shared by all instances

    # Constructor
    def __init__(self):
        print("__init__ of Parent")
        self.value = "Inside Parent"

    @staticmethod
    def _show():
        print("show() of Parent")

    # Parent's show method
    @staticmethod
    def show():
        __class__._show()
        print(__class__.custom_str)


# Defining child class
class Child(Parent):
    custom_str = "custom_str2"
    # Constructor
    # def __init__(self):
    #    self.value = "Inside Child"

    # Child's show method
    # def show(self):
    #     print(self.value)

    @staticmethod
    def _show():
        print("show() of Child")


# Driver's code
# obj1 = Parent()
# obj2 = Child()

Parent.show()
Child.show()

cls_list: list[type[Parent]] = [Child]

for cls in cls_list:

    @staticmethod
    def show():
        cls._show()

    cls.show = show

# obj3 = Child()
Child.show()
print(Child.__dict__)

print(Child.__name__)
print(Child.__qualname__)
Child.__name__ = "Child2"
Child.__qualname__ = "Child2"
Child2.show()
Child.show()
