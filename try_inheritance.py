# From https://www.geeksforgeeks.org/method-overriding-in-python/#
# Python program to demonstrate
# method overriding


# Defining parent class
class Parent:
    # Constructor
    def __init__(self):
        print("__init__ of Parent")
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):
    ...
    # Constructor
    # def __init__(self):
    #    self.value = "Inside Child"

    # Child's show method
    # def show(self):
    #     print(self.value)


class GrandChild(Child):
    ...


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

print(issubclass(Child, Parent))
print(issubclass(GrandChild, Parent))
