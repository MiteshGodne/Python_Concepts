# List -> represents group of individual objects as a single entity where
# Insertion order preserved - indexing applicable
# Duplicate objects are allowed
# Heterogeneous objects are allowed.
# Growable using __add__() and remove() 
# Mutable Object.


# Creation of Lists - 
# -> l = []
# -> l = [10,20,30,40]
# -> l = list([1,2,3,4,5])
# -> l = list((1,2,3,4,5))
# -> l = list(range(0,10,2))
# -> l = eval(input("Enter List:"))   # enter with [] and comma
# -> l = str.split("separator")


# Accessing of List Elements - 
# -> using index  -> l[0]
# -> using slice operator -> l[ start : stop : jumpIndex ] = [,,]
lis = ["apple", "banana", "cherry"]
lis[1:3] = ["watermelon"]
print(lis)    # Output - > ["apple","watermelon"]   # cherry will dlt

# Traversing List - 
# -> for loop  -> using membership operator => for ele in list
# -> for loop  ->  using list[index]   => for i in range(len(list)) 
# -> while loop  
    

# Operators on List
# -> l1 + l2 -> used to concatenate 2 lists only
# -> l * n -> repeats the list n times
# l1 == l2 -> True only if number, order and content are same 
# l1 < l2 -> Only 1st element is compared
# element in l -> True if element is present in list
# element not in l -> True if element is not present in list


# List Aliasing - Changes in one ref changes the actual list 
l = [10,20,30]
newRef = l

# List Cloning - exactly duplicate independent object
clone = l.copy()


