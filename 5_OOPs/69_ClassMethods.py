# Class Methods - 
'''
>>> A Class methods is a type of method that is bound to the class & not the instance of the class.
>>> Defined using @classmethod decorator, followed by the function definition.
>>> The first argument of class method is always 'cls' that represents the class itself.
>>> Class methods can be used to change the class variables.
'''
class Employee:
    company = "Apple"
    def show(self):
        print(f"Employee is {self.name} & company is {self.company}")
    # @classmethod
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employee()
e1.name = "Abeer"
e1.show()

e1.changeCompany("Tesla")  # class variable is not changed instead instance variable is created if @classmethod is not used. If @classmethod decorator is used then the method will take class as argument and changes the class variable.
e1.show()  
print(Employee.company)  


'''
>>> Class method can be defined to create instances of the class & return it to the caller.
>>> It can acts as an alternative constructor when we have different types of data to handle.
>>> For eg. if we have data in a single string then we have to parse it to fetch data.
>>> Hence, we use class methods to handle specific typed of data in alternate constructors.
>>> date time package has similar additional constructor for eg. fromTimeStamp() to fetch date.
'''
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

string = "Abeer-22"
# Parsing string to fetch name and age
s = Students(string.split("-")[0], int(string.split("-")[1]))
print(s.name, s.age) 

'''>>> Above code can be optimized using the following code - '''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
string = "John-22"
# using alternate constructor 
s2 = Student.from_string(string)
print(s2.name, s2.age) 
# NOTE - remember to type cast in classmethod if any data is of specific type


class Human:
    @classmethod
    def from_string(cls):
        print(type(cls))
h = Human()
h.from_string()  # <class 'type'>