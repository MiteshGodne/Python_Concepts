# Parameters can be ->

# A] Actual Parameters - Defined and used within the main program. 
# B] Formal Parameters - Defined and used within the function.


# Parameters can take ->
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


# Specifying types of arguments that can be passed ->
 
# 1) Positional-Only Arguments - To specify that a function can have only positional arguments, add (,/) after the arguments 
def my_function(x, /):
  print(x)
my_function(3)

# 2) Keyword-Only Arguments - To specify that a function can have only keyword arguments, add (*,) before the arguments.
def my_function(*, x):
  print(x)
my_function(x = 3)

# 3) Combined-Type Arguments - Any argument before the (,/) are positional-only, and any argument after the (*,) are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)