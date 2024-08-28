# Set -> represents group of individual objects as a single entity where
# Insertion order not preserved- no indexing.
# Duplicate objects are not allowed
# Heterogeneous objects are allowed.
# Set is Mutable & Growable using add() and remove() 
# Unchangeable - elements cannot be changed (no indexing allowed).



# Creation of sets - 
# -> set = set() 
# -> set = {10,20,30,40}
# -> set = eval(input("Enter Set:"))   # enter with {} and comma
# -> set = set( range(0,10,2) ) 
# -> set = set( (list) )
s = {10,20,30,40,40,20}
s2 = {60,70,80}


# Accessing of Set Elements - 
# -> using index ==> # Can give Type Error
# -> using slice operator [ : : ]  ==> Type Error


# Traversing Set - 
# -> for loop   for x in set
# -> while loop
# -> using index in for loop    for i in range(len(set)) 



# Set Comprehension - create a set based on existing set / values
# syntax - newSet = [ expression for x in iterable if condition == True ]
s = {x*x for x in range(1,6)}
print(s)
print(type(s))


# Set Aliasing - Changes in one ref changes the actual set 
s = {10,20,30}
newRef = s
print(type(s))

# Set Cloning - exactly duplicate independent object
clone = s.copy()

set = set()
set.pop()
