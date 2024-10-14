# dir() - This method is used for object introspection. It returns the " list of methods, dunder methods and attributes " of an object.
# If called without an argument, return the names in the current scope. Else, return list of names comprising the attributes of the given object, and of attributes reachable from it. 
z = [1,2,3]
print(dir(z)) 
t = (2,3,5)
print(dir(t))

# __dict__ - This attribute returns a dictionary representation of an object's attribute. It is used for introspection where all items assigned using self is shown. Dictionary for instance variables.
class Person:
    def __init__(self, age):
        self.age = age
    def greet():
        print("Hello")    
    
p = Person(22)
print(p.__dict__)       # {'age' : 22}


# help() - This method is used to print the help documentation for an object, including description of its attributes and methods. It returns None.
help(p)
   