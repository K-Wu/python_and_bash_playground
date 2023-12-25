# From https://www.geeksforgeeks.org/method-overriding-in-python/#
# Python program to demonstrate
# method overriding


# Defining parent class
class Parent:
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


# Defining child class
class Child(Parent):
    ...
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
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


for cls in [Child]:

    @staticmethod
    def show():
        cls._show()

    cls.show = show

obj3 = Child()
obj3.show()
