# Functions - It is a subprogram (blue block statement) used to perform that performs a specific & well defined task whenever it is called and compute the values.It is created using def keyword.

# A] Built in Functions ->
''' print(), id(), input(), range(), min(), max(), len()'''

# B] User Defined Functions -> using def keyword 
''' functions that user defines and calls'''
num1 = 9
num2 = 8
def har_mean():
    return 2*(num1*num2)/(num1+num2)
print(f"Harmonic mean is : {har_mean()}")


''' Declaration of Function'''
# pass keyword -> 
''' 
>>> used to declare function name with arguments without its body, as without body interpreter will throw indentation error.'''
def later():
    pass
def later():
    print("I am later")
later()

# return statement -> 
'''
>>> it returns one value from the function to the place where the function is called.
>>> it can also return multiple values in the form of tuple   # t1 = return (x,y,z)
>>> function returns None if return is not used'''

# yield statement -> 
'''
>>> It pause the execution of the function return the value to the caller and again starts the execution of the function.
>>> it can also return multiple values to from generator function
'''

