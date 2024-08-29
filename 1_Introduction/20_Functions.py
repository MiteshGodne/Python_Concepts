# Functions - It is a subprogram (blue block statement) used to perform that performs a specific & well defined task whenever it is called and compute the values.It is created using def keyword.

# A] Built in Functions ->
''' print(),id(),input(), range(), min(), max(), len()'''

# B] User Defined Functions -> using def keyword 
''' functions that user defines and calls'''
num1 = 9
num2 = 8
def geo_mean():
    return (num1*num2)/(num1+num2)
print(f"Harmonic mean is : {geo_mean()}")


'''Declaration of Function'''
# pass keyword -> 
''' 
 => used to declare function name with arguments without its body, as without body interpreter will throw indentation error.'''
def later():
    pass
def later():
    print("I am later")
later()

# return statement -> 
'''
 => it returns one value from the function to the place where the function is called.
 => it can also return multiple values in the form of tuple   # t1 = return (x,y,z)
 => function returns None if return is not used'''


# Anonymous Function / Lambda Function : Sometimes we can define the function without name, such functions are called lambda function / anonymous functions / nameless function / unnamed functions. Defined using lambda keyword. It cannot be of multiple lines.

# Syntax ->> lambda argument_list : expression
sum = lambda a,b : a+b
print(sum(10,20)) # returns 30
# OR
s = lambda : print("Hello")
print(s()) # returns none

# Usage ->> Sometimes we need to pass function as an argument to another function such as in filter(), map(). Here we use lambda function to reduce the code size and make it compact.
# without using filter, to get even list, the code is :-
l = [5,10,15,20,25,30]
def even(a):
    if(a%2==0):
        return True
    else:
        return False
evenNums = list(filter(even,l))

# 1) filter (function, sequence) - It filters the value from the sequence based on the condition given in function. 
evenList = list(filter(lambda a : True if a%2==0 else False, l))
# OR
evenList = list(filter(lambda a : a%2==0, l))
print(evenList) 


# 2) map() - It is used to apply the functionality to every element present in the sequence.
l = [5,10,15,20,25,30]
doubles = list(map(lambda a : 2*a, l))
print(doubles) 


 
