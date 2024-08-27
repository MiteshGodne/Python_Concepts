# Tuple -> represents group of individual objects as a single entity where
# Immutable - cannot add/remove elements. 
# Unchangeable - cannot assign new values. # Type Error.
# Insertion order preserved - indexing applicable
# Duplicate objects are allowed.
# Heterogeneous objects are allowed.

# Creation of tuples - 
# -> t = ()
# -> t = (10,) OR 10,   # else it will become int 
# -> t = (10,20,30,40)   OR t = 10,20,30,40
# -> t = tuple( range( 0,10,2 ) ) 
# -> t = tuple( (tuple) ) # double ()
# -> t = tuple( [list] )
# -> t = eval(input("Enter tuple:"))   # enter with brackets () and comma ,


# Accessing of Tuple Elements - 
# -> using index (both +ive and -ive)
# -> using slice operator [ : : ]


# Traversing tuple - 
# -> for loop  ->  for x in tuple
# -> using index in for loop -> for i in range(len(tuple)) 
# -> while loop 


# Operators on tuple -
# -> t1 + t2 -> used to concatenate 2 tuples only
# -> t * n -> repeats the tuple n times
# t1 == t2 -> True only if number, order and content are same 
# t1 < t2 -> Only 1st element is compared
t = (1,30,5,6,7)
t2 = (10,)
print(t>t2) # False
# element in t -> True if element is present in tuple
# element not in t -> True if element is not present in tuple

# To Modify Tuple, We must create a copy of tuple as list and again convert that modified list into tuple