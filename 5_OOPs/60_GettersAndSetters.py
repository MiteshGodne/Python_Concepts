# Getter Methods ->
'''
>>> Getters property decorators that return value of object's properties as getters acts ab properties. 
>>> Getter are used to access the value of an object's properties.
>>> They are defined using @property decorator.
>>>  
'''
class MyClass:
    def __init__(self, val):
        self.value = val 
        
    # defining property decorator   
    @property
    def getter(self):
        return self.value
    
obj = MyClass("Abeer")
print(obj.getter) # Abeer


# NOTE- we cannot modify getter hence we use setters to update the property values


# Setter Methods ->
'''
>>> Setters are methods that are used to modify the properties of an object.
>>> Setters are defined using @propertyName.setter where propertyName is the name of a getter function.
'''
class MyClass:
    def __init__(self, val):
        self.value = val
    
    # defining property getter
    @property
    def getValue(self):
        return self.value
    
    # defining property setter
    @getValue.setter
    def setValue(self, new_value):
        self.value = new_value 

obj = MyClass("John") 
print(obj.getValue)  
obj.setValue="Abeer"
print(obj.getValue)  
    