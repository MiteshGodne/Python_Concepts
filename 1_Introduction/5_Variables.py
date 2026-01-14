''' Variables -> Container that stores some data.'''
# _variable_name = value
# $ cannot be used to start variable name

# Multiple Assignment
a,b,c = 10,20,30
print(a,b,c)

# One value to Multiple Variables
a = b = c = 20
print(a,b,c)

# Unpack a Collection
list1 = ["hello", "world"]
x,y = list1
print(x,y)

# Type Error - Not Allowed to add incompatible object using +
# cantRun = "Abeer" + 5  # Type Error

# global keyword is used to access global variable inside a function with local variable of same name

'''Reference of another object'''
x = 10
y = x
y = 30
print(x)
print(y)

'''Constants are not applicable'''
# It is a convention to denote constants in CAPITALS
PI = 3.14
PI = 4.56  # Possible but not recommended
print(PI)