# dict -> represents group of individual objects as key : value pairs where
# Python 3.7 -> Dictionaries are Ordered indexing not applicable
# Python 3.6 -> Dictionaries are Unordered
# Duplicate keys are not allowed but values are allowed.
# Heterogeneous objects are allowed.
# Mutable Object.
# Changeable / Modifiable

# Creation of dict - 
# ->> d = {}   # Empty Dict
d = {100:'Olive' ,200:'Rocky', 300:'Ram'} # number key can be created here
# ->> d = dict()  # dict() constructor
# ->> d = dict(name="Abeer", age = 21 )   # Pass key = value as keyword arguments in dict() constructor  # number key cannot be passed
# ->> d = {"key1":"value", "key2":"value"}
# ->> d = eval(input("Enter dict:"))   # enter with {"":"","":""} and comma
# ->> d = dict(range(0,10,2))
# ->> d =  dict([(1,2),(3,4)])

# Modifying a dict -
# -> d[key] = value
# -> d.update(key);
# -> d[wrongKey] = value --> adds a new key:value pair
 

# Accessing of dict Elements -  
# -> using key -->dicts["key"] -> Produces Key Error if not found
# NOTE - .get() method returns None if key is not found
# -> using slice operator [ : : ] --> Key Error


# Traversing dict - 
# -> for loop   for x in dict
# -> while loop


# Operators on dict
# d1 == d2 -> True only if key and values are same 
# element in d -> True if element is present in dict
# element not in d -> True if element is not present in dict


# Deleting Elements -
del d[100]    # delete key : value pair else Key Error
print(d)  
# del d   # deletes dict and now it cannot be accessed - Name Error


# dict Aliasing - Changes in one ref changes the actual dict 
newRef = d


# dict Cloning - exactly duplicate independent object
clone = d.copy()
clone = dict(d)

