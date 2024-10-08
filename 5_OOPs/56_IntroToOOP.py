# Object Oriented Programming - everything in python is an object. Here we use classes and objects to represent real world entities.
""" Pillars of OOP -> 
>>> Class = object constructor = blueprint of the objects. 
>>> Object = real life entity = instance of a class.
>>> Encapsulation = internal state of an object is hidden and can only be accessed or modified using object methods.Getter & Setter are examples of encapsulation as they hides data.
>>> Inheritance = New classes can be created that inherits the properties and methods of an existing class.
>>> Polymorphism = Objects of different classes can be treated as if they were objects of a common class.
>>> Abstraction = Various access modifiers can be used for hiding unnecessary details of the program.
"""

# Creating Class with variables & methods
class Person:
    name = "Abeer"
    age = "22"
    occupation = "Software Engineer"
    def info(self):  # self refers to the current instance
        print(f"{self.name} is a {self.occupation}")

# Creating Object using class constructor
a = Person()

# Accessing variables using object.var
print(a.name, a.age, a.occupation)

# Calling methods using object.method() 
a.info()

# Modifying object variables
a.name = "Lokesh"
print(a.name)

# deleting object properties
del a.name

# deleting object
del a


''' self parameter ->
>>> self parameter is a reference to the current instance of the class, and it is used to access the variables that belongs to the class.
>>> It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
'''