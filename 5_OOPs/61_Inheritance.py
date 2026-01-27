# Inheritance :
'''
>>> Concept where a child class inherits all the public and protected properties and methods from the parent class.
>>> It can also have its own properties and methods.
>>> Syntax - class Child_Class(Parent_Class):
>>> Child object can access Parent's and its own methods & properties.
>>> Parent object cannot access child's methods and properties.
''' 

# Single Inheritance
class Employee:
    # name = "Default User"
    # id = "1000"
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"Name : {self.name},  ID : {self.id}")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    def showInfo(self):
        print(f"Name : {self.name}, ID : {self.id}, Language : {self.lang}")

p = Programmer("Raj", 10001, "python")
p.showInfo()
p.showDetails()


# Multilevel Inheritance - Multiple single inheritances
        
# Multiple Inheritance 
class MobileOrganisms:
    pass
class LivingBeings:
    pass
class Human(MobileOrganisms, LivingBeings):
    def show():
        print("I can move cuz I am alive")

"""NOTE - mro() method called on the Child class directly to get the method recognition order of various methods accessible to the objects of child class. In multiple inheritance a method is searched in current class and then searched in parents classes based on the order they are inherited."""
print(Human.mro())

# Hybrid Inheritance - Combination of different inheritances

# Hierarchical Inheritance - Multiple subclasses inherited from same parent class.