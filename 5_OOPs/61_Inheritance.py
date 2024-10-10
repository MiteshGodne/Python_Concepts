# Inheritance :
'''
>>> Concept where a child class inherits all the public and protected properties and methods from the parent class.
>>> It can also have its own properties and methods.
>>> Syntax - class Child_Class(Parent_Class):
>>> Child object can access Parent's and its own methods & properties.
>>> Parent object cannot access child's methods and properties.
''' 


class Employee:
    name = "Default User"
    id = "1000"
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"Name : {self.name},  ID : {self.id}")

class Programmer(Employee):
    def __init__(self, lang):
        self.lang = lang
    def showInfo(self):
        print(f"Name : {self.name}, ID : {self.id}, Language : {self.lang}")
  
p = Programmer("java")
p.showInfo()
p.showDetails()
