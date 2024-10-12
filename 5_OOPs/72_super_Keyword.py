# super -
''' 
>>> It is used by child class to call parent class methods as super refers to the parent class.
>>> It is used when a child inherits multiple classes and needs to call a methods of a parent class.
>>> It is used when child class overrides parent method & we want to call parent method.
>>> Also used to call parent constructor.
'''
class Parent:
    pid = "101"
    def __init__(self, name):
        self.name = name
    def parent_method(self):
        print("I am a parent method")
    def greet(self):
        print("hello")

class Child(Parent):
    pid = "201"
    def __init__(self, name, age):
        super().__init__(name)     # calling parent constructor
        self.age = age
    def parent_method(self):
        print("Child class ")      # Override & modify parent method
        super().parent_method()    # calling parent method
    def child_method(self):
        print("I am a child method")
c = Child("Abeer", 22)
c.child_method()
c.parent_method()
c.greet()
c2 = Child("Lokesh", 22)
