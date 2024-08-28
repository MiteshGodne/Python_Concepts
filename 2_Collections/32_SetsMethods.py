s = {10, 20, 30, 40, 70, 80}
s2 = {10, 20 , 30, 50, 90}


# Operators on Set -> 

s.union(s2) 
# multiple sets can be passed
# OR
union = s|s2 # returns combined set union

s.intersection(s2)  
# OR
intersect = s&s2  # returns common elements only 

print(s.isdisjoint(s2))
# True if they are disjoint i.e. they dont have intersection / common elements 

print(s2.issubset(s)) # True if s is a subset of s2   ==>  s2<=s
print(s.issuperset(s2)) # True if s is a superset of s2

s.intersection_update(s2)
# removes elements from s which are not common in s & s2 ==>  s>=s
print(s)

s.difference(s2)  # OR 
diff = s-s2  # returns elements in s which are not in s2
print(diff)

s.difference_update(s2)  
# Removes elements from s which are common in s and s2 
print(s)

s.symmetric_difference(s2)  # OR
s^s2 # Returns elements present in either x or y but not in both

s.symmetric_difference_update(s2)
print(s)
# Inserts symmetric difference elements in s from both s & s2, Also removes common elements from s
# ^= symbol can also be used  

print( 100 not in s2)
print( 30 in s)  


# Set Methods - 

len(s)

min(s)
max(s)

s.add(100) # adds elements into set

s.update(s2) # list,tuple,range(5) i.e. Any iterable arguments
# OR |= is the symbol used for update()

s.remove(3)    # remove element  else  Key Error

s.discard(20)   #  remove element  else does not produce error

s.pop()   # returns random element  else Key Error

print(s.clear())   # removes all the elements -> returns none and makes set empty

# Deletes the whole set
del s2  
