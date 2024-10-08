# Constructor - 
'''
>>> Constructor is a special method in a class used to create & initialise an object of a class.
>>> Constructor can be created using 'def __init__(self)'
>>> Object itself is passed implicitly as an argument hence, at least 1 parameter is must to declare else it produces TypeError.
>>> It does not have to be named self, any name can be used, but it has to be the first parameter of any function in the class.
>>> Constructor is invoked automatically when an object of a class is created.
>>> __init__() cannot return any value other than None. 
'''

# Default Constructor - no explicit arguments are passed
class Student:
    def __init__(self):
        print("I am a constructor")
s1 = Student()

# Parameterized Constructor - arguments passed explicitly
class Calculation:
    def __init__(self, a, b ):
        self.num1 = a
        self.num2 = b
c1 = Calculation(10,20)
print(c1.num1)


# __str__(self) - 
'''It is a dunder/magic method that controls what should be returned when class object is represented as a string.'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
p1 = Person("John", 36)
print(p1) # <__main__.Person object at 0x0000025D4C1C6660>
 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} of {self.age}"

p1 = Person("John", 36)
print(p1) # John of 36  