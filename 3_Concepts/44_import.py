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

# we can import any custom python file to access its functions and variables 
from practice import func
func()

