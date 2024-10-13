'''
>>> Module is a group of variables, functions and classes saved in a file.
>>> Every python file saved with .py extension act as a module.
>>> Library => Group of Modules.
1] math
2] os
3] time
4] importlib
5] pypdf
>>>
'''

""" built in modules """
# Importing is a process of loading & executing code from a python module into the current script 
import math

# functions and variables can be used using dot operator with module name
print(math.sqrt(144))

# from keyword is used if we want to import only certain specific function or attribute 
from math import floor

# import multiple functions or modules using , 
from math import floor,sqrt
print(floor(19.3))

# import all the functions and variables and we will not need dot operator to use functions 
from math import *
print(sqrt(100))

# as keyword to rename the function, module or variable imported
import pandas as pd

# dir() function - used to see all the functions and variables defined in a module
print(dir(math))


"""Custom Modules"""
# we can import any custom python file
import myModule 

# we can import any module functions, classes and variables. 
from myModule import greet
greet()


# Preventing automatic module execution - 
'''
>>> just by import module command, the whole module is executed and if the module contains function call or object creation etc, they all are executed.
>>> to prevent automatic execution of a module while import, add a condition if __name__ == reqFileName
>>> __name__ returns the current file name which had executed it.
'''
print(__name__) # returns __main__ if 45__name__.py is run else 45__name__.py if it is executed by any other module

# Reloading Module - 
'''
>>> When a module is imported, its members are loaded into the memory. and if modifications are made into imported module the modifications are not imported automatically.
>>> Python 3.4 : we use 'reload()' function of 'imp' module to reload the modified module into a memory.
>>> Python 3.7 : we use 'reload()' function of 'importlib' module to reload the modified module into a memory as 'imp' module is deprecated.
'''
from importlib import reload
reload(myModule)
