'''Type Casting / Coercion = conversion of one data type into other data type. '''

# 1. Implicit Type Casting - Python interpreter only converts lower order data types into higher order data types automatically during operations. 
# int + float ==> float
# str + char ==> str

# 2. Explicit Type Casting - User uses various functions for type casting -
# a] int()   // cannot convert chars or complex numbers into int but converts string if it only has numbers
# b] float()
# c] str()
# d] chr()  // integer to valid character
# e] oct()
# f] hex()
# g] tuple()
# h] set()
# i] list()
# j] dict()
# k] ord()  // convert char into integer unicode code
# l] complex(r,i)  only works with numbers 


'''int, float, bool, str, complex, tuple are immutable'''


''' type() function -> it is used to get the type of data a variable stores. Since everything in python is an object, hence printing type will print the class to which the data belongs. '''
print(type("Hello")) 
print(type(21))
print(type(20.2))
print(type(10j))   # complex
print(type(True))  # bool
print(type(None))   # NoneType
print(type([1,2,3]))  # list
print(type((1,2,3)))  # tuple
print(type(range(6)))  #range
print(type({"name":"Abeer"}))  # dict
print(type({"Sharma","Abeer"})) # set
print(type(frozenset({"abeer","sharma"})))  # frozenset
print(type(b"hello")) # bytes
print(type(bytearray(5))) #bytearray
print(type(memoryview(bytes(5)))) # memoryview


