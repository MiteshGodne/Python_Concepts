''' Data Types : Data type specifies the type of data a variable can store. There is a class for every data type in python.
'''

# 1. Numeric Data -
# a] class int => Integer 
# It can be of different types - 
age = 21     # decimal type
print(age)
binary = 0b111 # starts with 0b / 0B
print(binary) 
octal = 0o123 # starts with 0o / 0O
print(octal)
hexadecimal = 0x1a  # starts with 0x / 0X
print(hexadecimal)

# Note - Gives syntax error if invalid number is written eg - 0b11012

# b] class float => Floating Point 
height = 5.11    
exponentialForm = 1.2e4   # 1.2 * 10000
print(exponentialForm)

# c] class complex => Real Number with imaginary part (j)
# real part can be specified in octal, binary & hexadecimal form but not imaginary part.
complexNo = 3-5j 
print(complexNo)  # (3-5j)
complexNum = complex(0.8,0.2)
print(complexNum) 
# attributes of complex numbers to retrieve a part - 
print(complexNum.real)
print(complexNum.imag)



# 2. Text Data - 
# class str => 
# single line string  with " " Or ' '
name = "Abeer"
surname = "Sharma"
# multi line string  with """  """ Or '''  '''
address = '''scheme
no 178'''
print(address)



# 3. Boolean Data -
# class bool => True = 1 & False = 0
isStudent = True
print(True+True)     # prints 2



# 4. None -
# class NoneType 
backlog = None



# 5. Sequence Data -
#  list => Collection of elements 

# a] class list = Collection of same/different data elements where insertion order is preserved and duplicates are allowed and is mutable and growable
list = [name,age,isStudent,backlog, [1,2,3]]


# b] class tuple = Similar to list but Immutable ie read only version of list
tuple1 = (name, surname, "Mango", "Mango", name)
print(tuple1)  
# OR
tuple2 = name, surname, "Mango", name

t1 = 10,   # tuple with single element ends with ','
print(type(t1))

# c] range(start,stop,step) - represents sequence of nos.
nums = range(10)
print(type(nums))


# 6. Mapped Data = dict
# class dict => key : value pairs where insertion order is not preserved but dict is mutable
dict = {'name':"Abeer", "age" : 21, "canVote" : True}
print(dict)

d = {}   # empty dict
print(type(d))   # class dict  


# 7. Set Type Data - stored group of data where insertion order is not preserved and duplicates are not allowed and is mutable and growable but indexing is not applicable
# a] set
mySet = {"apple", "banana", 30, 4.56}
print(mySet)

s = set()   # to create an empty set  
print(type(s))


# b] frozenset
myFrozenSet = frozenset({"apple", "banana", "cherry"})


# 8. Binary Data Types - used to represent images and video type binary content
# a] bytes - group of byte numbers just like an array
x = [10,20,30,40]
b = bytes(x)
print(x[0])
print(x)

# byte does not support item reassignment in array form
# b[0] = 50  # error

# to make a string in byte format
x = b"Hello"
print(x)

# b] bytearray - supports item reassignment.
y = bytearray([5,6,7,8])
y = bytearray(x)
y[0] = 20
print(y)   # prints numbers in hexadecimal format
# for loop can be used to print all the values 1 by 1 


# c] memoryview
z = memoryview(bytes(5))








