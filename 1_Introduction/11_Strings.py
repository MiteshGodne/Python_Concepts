''' 
Strings = collection of characters inside "" or '' or ''' '''.
Strings are immutable hence they cannot be changed in place, so if we try to change it, new string is created.'''

# Types of String - 
singleLine = "Hello, World !!"
print(singleLine)
multiLine = """You can use triple quotes 
to make a multi line string as it allows line breaks"""
print(multiLine)



names = "Abeer,Mitesh,Lokesh"
# Length of String =>  len() function can be used
print(len(names))


# Accessing Characters of String - done using 0 based indexing inside square brackets[]
# a] Positive indexing {0 to len(str)-1} left to right 
print(names[0])   
# b] Negative indexing {-1 to len(str) } right to left
print(names[-19])   



# Slicing of Strings =>  [start_index : end_index : step] can be used
print(names[0:5])  # 5 index will be excluded
print(names[:5])   # 0 is used as start_idx by default
print(names[:])  # 0 to len() - 1 
print(names[:-3])  # 0 to len() - 3 => 0 to 16
print(names[-1:-3])  # len() - 1 to len() - 3 => 18 to 16 {which is not possible so it prints blank line}
print(names[-3:-1])  # len() - 3 to len() - 1 => 16 to 18  {18th index is excluded} 
print(names[0:18:2]) # increment is 2 so it skips 1 index every time, by default is 1 so it increases by 1 so it does not skip any index


# Reverse a string =>
print(names[::-1]) 


# Arithmetic Operations on string
# + concatenation
# * repeats string


# Membership Operator - to check substring / char
print("Abeer" in names)  # True

# Comparison Operator - < , > , <= , >= , != , ==  based on alphabetical order


# Note 
# => string index out of range occurs if index exceeds the string size
# In the backward direction (step = -1) if end value is -1 then result is always empty.
# In the forward direction if end value is 0 then result is always empty.
