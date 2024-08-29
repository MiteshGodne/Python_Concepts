# Functions - It is a subprogram (blue block statement) used to perform that performs a specific & well defined task whenever it is called and compute the values.It is created using def keyword.

# A] Built in Functions ->
''' print(),id(),input(), range(), min(), max(), len()'''

# B] User Defined Functions -> 
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



# Parameters can be ->
# 1] Actual Parameters - Defined and used within the main program.
# 2] Formal Parameters - Defined and used within the function.

 
# Arguments / Actual Parameters can be ->

# 1] Default Arguments - default values
'''
 => default values which are used if function is called without arguments.'''
def defaultArgs(a = 0, b = 0):
    print(a+b)
defaultArgs()    # both default values are used
defaultArgs(5)   # default value of b is used
defaultArgs(b=9) # default value of a is used 

# In python positional parameters 

# 2] Keyword Arguments - Position/order not required
'''
 => Arguments can be passed in key=value form so that interpreter can identify it by parameter name & hence order is not necessary. 
 => this way we can change the order of arguments passed'''
def keywordArgs(name, age):
    print(name,"is",age,"years old")
keywordArgs(age=21,name="Abeer")


# 3] Positional arguments == Required Arguments in order -
'''
 => These are parameters which are passed in correct positional order.
 => when default values are not defined in the parameters than arguments becomes required arguments and interpreter will throw error if args not given.'''
def hey(name, age):
    print(name,age)
hey("Abeer", 21)


# 4] Variable Length Arguments - 
'''
 => In python we can pass n number of parameters 
 => used when we need to pass more arguments than those defined in the function, 2 ways are there to do so :-'''

# 4.a] Arbitrary Arguments - args as tuple
'''
 => pass * before the parameters in the function while defining. 
 => In this way the function accesses the arguments in the form of a "tuple".'''
def arbitraryFunc(* num):
    print(num[0], num[1])
arbitraryFunc(10,20)

#4.b] Keyboard Arbitrary Arguments - args as dict
'''
 => pass ** before the parameters in the function while defining.  
 => In this way the function accesses the arguments in the form of a "dictionary".'''

def keyboardArbFunc(** items):
    print(items['fname'],items['lname'], "is a good guy")
keyboardArbFunc(fname="Abeer", lname = "Sharma")

#OR

def function(** dicts):
    print(dicts)
function(name="Abeer",age=21,sex="M")


# Anonymous Function / Lambda Function : Sometimes we can define the function without name, such functions are called lambda function / anonymous functions / nameless function / unnamed functions.Defined using lambda keyword. It cannot be of multiple lines.

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


 
