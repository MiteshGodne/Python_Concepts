
# dict Methods - 
d={100:'Olive' ,200:'Ram', 300:'Rocky'}

len(d)
min(d)
print(max(d))  # prints key

d.clear()  # clears whole dict -> empty dict

d.get(100)   # gets the value associated with the key else None

d.pop(100)   # removes the key:value pair else throw Key Error

d.popitem()   # removes last inserted item from dict & returns it else key error

keys = d.keys()  # returns all the keys as obj of <class dict_keys>
print(type(keys))  

t = (100,200,400)
dictionary = dict.fromkeys(t) # returns a dictionary made from tuple elements as keys and values as None 
print(dictionary)


values = d.values() # returns all the values as obj of <class dict_values>
print(type(values)) 

d.items() # returns list of tuples representing key,value pairs
for k,v in d.items():
    print(k,":",v)

d.setdefault(100,"Abeer")   # returns Olive as 100 is available
d.setdefault(500,"Lokesh")  # returns Lokesh as 500 is not present

d2 = {100:"Amir"}
d.update(d2) # adds d2 to d1
print(d)


# deprecated in python 3 ->  d.has_key(100) so now we use -
print(100 in d)

sum(d.values())   # only sums integer values else TypeError

# dict Comprehension - create a dict based on existing dict / values
# syntax - newDict = [ expression for x in iterable if condition == True ]
squares={x :x*x for x in range(1,6)}
print(squares)

del d["fe"]  # deletes key:value else key error

del d # deletes complete dict else name error

