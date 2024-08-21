# Formatting of String / Literal string Interpolation - Python 3.6
'''
=> Embed python expressions inside the string.
=> Operating on strings with other incompatible data types. 
=> To specify a string as f-string 
===> add curly brackets {} as placeholders for variables, operators, functions and modifiers inside the string.
===> simply put an f in front of the string literal.
'''

# For Example ->
name = "Abeer"
print(f"My name is {name}")

# placeholders can also contain modifiers {:.2f} is a modifier used to print 2 digits after decimal ->
age = 21.9
txt = f"I'm {age:.2f} years old."
print(txt)


# .format() function ->
'''"string with {0}".format(variable) can also be used where string contains {replacementIdx} and format() contains variable to put in-> '''
salary = 1202
myTxt = "Abeer earns {0}".format(salary)
print(myTxt)
'''Note- writing number in {} is not mandatory'''

# Old Style ->
salary = 2311.232344324
print("I earn %d Rs"%salary)


# Docstring ->
'''
=> String literals that appear right after the definition of a function above the code body, method, class or a module for its description of input and output.
=> funcObjName.__doc__  is an attribute used to access the docstring '''

def average(*num):
    '''Takes numbers as input, returns their average''' 
    sum = 0
    for i in num:
        sum = sum + i
    return sum / len(num)

res = average(4,5,6,7)
print(average.__doc__)

