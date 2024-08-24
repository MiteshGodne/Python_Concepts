# List Methods - 
l = [10,20,30,40,40,20]
l2 = [50,40]
len(l)
min(l)
max(l)

# Accessing list
l.count(10)
l.index(30)    # returns index of element else Value Error


# Add elements
l.append(50)   # add element at last
l.insert(2,100) # insert(idx, element) -> If the specified index is greater than max index then element will be inserted at last position.
l.extend(l2)  # merges list with any iterable object - l,t,s,d
 

# Remove elements 
l.remove(30)    # first occurrence  else  Value Error
l.pop()   # returns last element  else Index Error
l.pop(2)   # removes index 2 element
l.clear()   # removes all the elements and makes it an empty list
del l2[2]  # deletes the list / index element else Index Error



# Alphanumeric Sorting using in-built sort() function
l.reverse()
l.sort()   # Ascending Sort else Type Error in Heterogeneous List
l.sort(reverse = True)  # Descending Sort
# Custom Sorting using a function
def myFunc(n):
    return n-50
l.sort(key = myFunc) 
# Sorting is case sensitive (capitals then smalls), to make it in-sensitive we can use custom sorting key keyword
l.sort(key = str.lower())


# List __add__ function : returns the combined lists 
l2 = [3,2,4,5,6]
l = l.__add__(l2)
print(l)


# List Comprehension - shortest syntax for looping lists or creating a list based on existing list / values.
# The return value is a new list, leaving the old list unchanged.
# syntax : li = [expression for item in iterable if condition == True]
# expression can be manipulated - [x.upper() for i in l]
# condition can be applied to exp - [x if x!=0 else "zero" for x in l]
l = [x for x in range(1,11) if x%2==0]
print(l)
print(type(l))
# OR
[print(x) for x in l]
