# Tuple Methods - 
t = (10,20,30,40,40,20)
t2 = (60,70,80)

# Fundamental Functions -
len(t)
min(t)
max(t)
id(t)
sum(t)


# Methods for Occurrences - 
t.count(10)   # no of occurrences
idx = t.index(10)    # returns index of 1st occurrence else Value Error
idx = t.index(30, 1, 3) 
# (element,start,end) to search index in a sub tuple  

# Delete the Tuple - 
del t2

# Sorting of Tuples - sorted() does not perform inplace sorting -> 
sortedTuple = sorted(t)   # Ascending Sort else Type Error in Heterogeneous Tuple
t3 = "a","B", "z","P"
sortedTuple = sorted(t3, key = str.lower)
# Sorting is case sensitive (capitals then smalls), to make it in-sensitive we can use custom sorting key keyword
sortedTuple = sorted(t,reverse = True)  # Descending Sort


# Tuple Packing 
a = 10
b = 20
c = 30
t = a,b,c
print(type(t))


# Tuple Unpacking - At the time of tuple unpacking the number of variables and number of values should be same, otherwise we will get ValueError.
a,b,c = t
# Note - if number of variables are unknown then add * which catches all remaining tuple elements in list form.
t = (1,2,3,4,5)
a,*b,c = t # a=1, b=[2,3,4], c = 5
print(c)


# Tuple Comprehension - Not supported as it returns generator object
t= ( x**2 for x in range(1,6))
print(type(t))
for x in t:         # loop is needed to print generator object elements
    print(x)

