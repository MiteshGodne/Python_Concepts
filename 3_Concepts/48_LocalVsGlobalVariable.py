''' Local variable - Variable declared inside a function inaccessible outside the function scope.''' 
def hello():
    num = 10
    print(num)    # Prints 10
hello()
# print(num)   ''' NOTE - Produces Name Error'''


'''Global variable - Variables declared outside the function, accessible inside the function.
'''
x = 4
print(x)   # Prints 4

'''global keyword -> used to create and change value of global variable inside the function.'''
def hello():
    global x 
    x = 5  # changing the value of global variable
    print(x)  # Prints 5
hello()
print(x)  # Prints 5







