# Lambda / Anonymous Function :
'''
>>> Sometimes we can define single line function without name, such functions are nameless lambda functions defined using lambda keyword. 
>>> It cannot be of multiple lines.
>>> Syntax -> lambda arguments : expression
>>> return keyword is not used.
'''
sum = lambda a,b : a+b
print(sum(10,20)) # returns 30
# OR
s = lambda : print("Hello")
print(s()) # returns none

'''
>>> Usage ->> Sometimes we need to pass function as an argument to another function such as in filter(), map(). Here we use lambda function to reduce the code size and make it compact.
'''