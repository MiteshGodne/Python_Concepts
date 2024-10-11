# Static Methods - 
'''
>>> Static methods are methods that belongs to a class instead of an object.
>>> Defined using @staticmethod decorator.
>>> Does not have requirement of self i.e. current instance while declaration, hence class name is used with class attributes.
>>> Static methods can be called using any object or class name.
>>> Used to create utility functions. 
'''

class CalculateBill:
    totalAmount = 0
    def __init__(self):
        self.totalAmount = 0
        
    @staticmethod
    def addAmount(amount):
        CalculateBill.totalAmount += amount

c = CalculateBill() 
c.addAmount(10)
CalculateBill.addAmount(20)
print(CalculateBill.totalAmount)
    

# Type Of Variables -
'''
>>> Instance variable - created when a variable needs to be associated with an object. Every object has its own copy of instance variable created while calling constructor.
>>> Class variable - created when a variable needs to be associated with the class along with all of its objects. 

NOTE - if class variable is modified using instance then actual value of class variable is not used instead instance variable with same name is created.
NOTE -  instance variable has more priority than class variable
    >>> if class variable is printed then PVM will first check if the object has instance variable with same name as class variable, & if present then instance variable is printed. 
    >>> if an object has not modified class variable then original class variable is printed.
    >>> class variable is changed only if it is modified using class name.
'''
class MyClass:
    classVar = "MyClass"
    def __init__(self):
        self.instanceVar = "myObj"

myObj = MyClass()
myObj.instanceVar = "I am instance variable"
print(myObj.instanceVar)   # I am instance variable

myObj.classVar = "I am class variable"
print(myObj.classVar)   # I am class variable
print(MyClass.classVar)   # MyClass 

MyClass.classVar = "Changed Value"
print(myObj.classVar)  # I am class variable 


# Function that prints list of all the attributes associated with tha class or object
# print(dir(MyClass))
print(dir(c)) 



