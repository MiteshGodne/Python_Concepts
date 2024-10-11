'''
>>> Access modifiers in python are used to limit the access of class variable and methods outside of class while implementing the concepts of inheritance.
>>> All the methods & variables are by default public.
>>> Python does not support private, public & protected keywords.
'''

# Public => Accessible to all objects of class & subclass directly.
'''
>>> Syntax -> objectName.variableName
'''
class Student:
    def __init__(self):
        self.name = "Abeer"
s = Student()
print(s.name, "is a good guy")

# Protected => Accessible to all objects of class & subclass directly.
'''
>>> Naming has been performed that the variable name prefix with single underscore which does not provide any actual protection
>>> Syntax -> objectName._variableName
'''
class Human:
    def __init__(self):
        self._ethnicity = "Asian"
class GenZ(Human):
    pass

s = Human()
print("He is ",s._ethnicity)  # class object

g = GenZ()
print(g._ethnicity)  # subclass object


# Private => 
'''
>>> There is no strict rule that prevents accessing of private variables. 
>>> Still a convention has been made that the variable name prefix with double underscore k/a Weak Internal Use Indicator. 
>>> Attribute Error is thrown if we try to access it directly using object.
>>> Private members can be accessed indirectly by adding _ClassName prefix with single underscore at beginning. 
>>> Syntax - objectName.__ClassName__variableName

NOTE - Name Mangling ->
>>> It is a process used to protect class and super class private attributes from being accidentally overwritten by the subclasses.
>>> Names are transformed by addition of single underscore for class private attributes and double underscore for superclass private attributes.
'''
class Employee():
    def __init__(self):
        self.__password = "10101"
    def __showInfo(self):
        print(self.__password)
        
e = Employee()
try:
    e.__showInfo() # AttributeError
    print(e.__password) # AttributeError
except:
    print("Cannot access private attributes.")
print(e._Employee__password)  # 10101
e._Employee__showInfo()  # 10101


