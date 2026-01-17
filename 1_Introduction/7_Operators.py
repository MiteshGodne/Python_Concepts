# Operators = Operators are used to perform operations on operands


''' Arithmetic Operators 
# +, -, *, /, %, 
# Integer & Floor Division (//)
# Exponential (**)
'''


'''Bitwise Operators
# { &  |  ^  ~ }
# { <<  >> }
'''


''' Assignment Operators   
# Arithmetic {  =  -=   +=  /=  *=  %=  //=  **= }
# Bitwise {  &=  |=  ^=  }
# Shift { >>=  <<= }
# Set Equal to { print(x : = 3) --> x = 3; print(x) }  
'''


'''Repetition Operator - When * is used between one string and one integer value n, it acts as repetition operator and the string is repeated n times'''
print("Hello "*3)


'''Identity Operator - It is used to check if the objects are same with same reference and not if they are equal. 
'''
name = "Abeer"
myName = "Abeer"

# a]  is -> Same Object  
print(name is myName)    # True because of string interning (immutable objects are reused with same value to save memory)

# b]  is not  
print(name is not myName)   # False

# Note - Value same but Objects are different
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)   # False

# Reference value of an object
print(id(list1))


'''Membership Operator - It is used to check if the sequence with the specified value is present in the object or not. 
'''
data = ["Abeer", "Sharma", 21]

# a]  in -> Same Object 
print("Abeer" in data)     # True

# b]  not in  
print("Abeer" not in myName)    # False


'''Comparison Or Relational Operators 
{ == >=  <=  <  >  != }
'''
# Strings can also be compared on Unicode basis. 
# Chaining of relational operators is possible.
print(10<20<30<40)    # returns True
print(10>True)  # True
print((10<20<30)==True) # True
print(("") != False) # True because "" is falsy value but of type str and not equal to False which is of type bool
a = 2
b = 3
print(a or b) # prints 2 because a is True in boolean context


'''Ternary Operator'''
x = 30 if a<b else 40
print(x)
# Nested Ternary Operator
min = a if a<b and a<x else b if b<x else x


'''Conditional Operator 
{ and  or  not }
'''


''' Slicing Operator [] => string[ startIdx : endIdx ] '''
myStr = "Hello"
print(myStr[0:40])  # no error prints 'Hello' as endIdx exceeds string length so it takes upto string length
print(myStr[4]) # prints 'o' single character at index 4
# print(str[40])  # error

# NOTE- '==' compares the value only whereas 'is' operator compares the actual address of the object, if address is same then only it returns True 
a = 3
b = a
print(a is b) # Immutable objects such as int / tuple / str / None with the same value are not created again rather new reference is assigned and hence "is" & "==" gives True
a = [1,2,3]
b = [1,2,3]
print(a is b) # Mutable objects are created with different address even if the values are same hence, "is" gives False but "==" gives True


'''Operator Precedence'''
# () 
# **
# unary , ~ 
# *, /, //, %
# +, -
# shift
# relational
# &
# ^
# |
# Comparison, Identity, Membership 
# not
# and
# or