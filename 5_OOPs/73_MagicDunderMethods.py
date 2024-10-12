# Magic / Dunder Methods -
'''
>>> These special methods are defined in class which gives powerful way to manipulate objects and their behavior.
>>> Dunder / magic methods begins and ends with double underscores.
>>> It can be called using obj.__dunderName__() or dunderName(obj).
>>> All Python operators, like +, ==, and in, rely on dunder methods to implement their behavior.
>>> These are basically used for operator overloading.
>>> Used to implement special methods such as addition, subtraction & comparison as well as advanced properties such as descriptors & properties.

'''
# __init__ -> It is a constructor method which gets called automatically for the object initialization. It can be overridden in the class.

# __len__ : It is a magic method which can  get the length of an object (size of a data structure such as list or dict) by passing the objectName. 
class Employee:
    name = "Abeer"
    # Overriding len attribute of object to return name length
    def __len__(self):
        i = 0
        for c in self.name:
            i=i+1
        return i
e = Employee()
print(e.__len__())
# OR 
print(len(e))


# __str__ -> It can be override to print customized string representation of an object. By default it prints <__main__.Student object at 0x000001E1E62F6000>
class Student:
    name = "Abeer"
    def __str__(self):
        return "This is __str__"
s = Student()
print(s)
# OR
print(str(s))
# OR 
print(s.__str__())


# __repr__ -> It is used to get string representation of an object which can be used to recreate the object.
class Student:
    name = "Abeer"
    def __repr__(self):
        return "This is __repr__"
s = Student()
print(s)
# OR
print(repr(s))
# OR 
print(s.__repr__())

# Note - If __str__ is not defined then it will fallback to __repr__ method.

# __call__ -> It is used to make an object callable, and parameters can be passed to it. It makes objects behave like functions.
class States:
    def __call__(self):
        print("Hi, I am callable obj")
stu = States()
stu()