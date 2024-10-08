# Generator is a function which is used to generate the sequence of the numbers. It pause the execution of the function return the value to the caller and again starts the execution of the function. It uses yield statement instead of return function.
# return statement executes one time but yield function executes multiple times.

def myFunc(n):
    for i in range(n):
    #    print(i)
       return i
res = myFunc(5)
print(res)

def myFunc(n):
    for i in range(n):
       yield i

# res stores multiple values so either convert it into list of use for loop to print all the values
res = list(myFunc(5))
print(res)