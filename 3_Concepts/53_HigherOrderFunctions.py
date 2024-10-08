''' >>> 1) filter (predicate, sequence) - It filters the value from the sequence based on the condition given in function and returns a new sequence as filter object. 
NOTE - predicate argument is a function argument that returns a boolean value
'''
# # without using lambda, to get even number list we write:-
l = [5,10,15,20,25,30]
def even(a):
    if(a%2==0):
        return True
    else:
        return False
evenNums = list(filter(even,l))
print(evenNums) 

# using lambda functions, the code becomes :-
evenList = list(filter(lambda a : a%2==0, l))
# OR
evenList = list(filter(lambda a : True if a%2==0 else False, l))
print(evenList) 


''' >>> 2) map(function, sequence) - It is used to apply the functionality to every element present in the sequence, and returns a new sequence as a map object.
'''
# without lambda function, the code is - 
l = [5,10,15,20,25,30]
def doubler(a):
    return 2*a
result = list(map(doubler, l))
print(result)

# using lambda function, code shortens to -
doubled = list(map(lambda a : 2*a, l))
print(doubled) 


''' >>> 3) reduce(function, sequence, initial) - It applies a function to first 2 elements, then their result to the next element and so on. It returns a single value.
NOTE - for n elements in sequence, reduce calls the function n-1 times.
NOTE - reduce needs to be imported from functools module.
'''
from functools import reduce
# without lambda function, the code is - 
l = [10,10,10,10]
def sum(a,b):
    return a+b
total = reduce(sum,l)
print(total)

# using lambda function, code shortens to -
total = reduce(lambda a,b: a+b, l)
print(total)  
