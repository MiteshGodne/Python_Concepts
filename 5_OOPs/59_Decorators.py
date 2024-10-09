# Decorator is a function which takes the function as an argument and extend its functionality and return the modified function with extended functionality.
# They are used in logging functions to log the arguments & return the value of function after importing logging module.
    
# Steps - 
''' 
>>> first write a decorator function with any identifier, pass another identifier as formal parameter.
>>> define another modifiedFunc function which has the added functionality in decorator function which should return original function if added functionality is not used.
>>> return modifiedFunc function from decorator function.
>>> use @ decorator_function_name before declaring the original function.
'''
def decor(func):
    def modifiedFunc(name):
        if(name=="Abeer"):
            func(name)
            print("Where were you ?")
        else:
            return func(name)
    return modifiedFunc

@decor
def wish(name):
    print("Hello",name, "Good Morning")
wish("Abeer")

# If @decor is not used then we have to explicitly pass our function to decorator function and its arguments in another parenthesis.
def decor(func):
    def modifiedFunc(name):
        if(name=="Abeer"):
            func(name)
            print("Where were you ?")
        else:
            return func(name)
    return modifiedFunc
def wish(name):
    print("Hello",name, "Good Morning")
decor(wish)("Abeer")

# NOTE- arguments, *args or **kwargs can be passed to modifiedFunc(args / *args /**kwargs) inside decorator function and pass their values in a separate parenthesis of decorator function after the function passed.