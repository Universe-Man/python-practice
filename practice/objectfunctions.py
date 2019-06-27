class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")
    def someMethod(self):
        print("Hello")

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Object Created")

parent = ParentClass()
child = ChildClass()

isinstance(parent, ParentClass)
isinstance(5, int)
isinstance(child, ParentClass)
isinstance(parent, (ParentClass, int))
isinstance(parent, ChildClass)


try:
    isinstance(parent, MyClass)
except NameError:
    print("No such class")
