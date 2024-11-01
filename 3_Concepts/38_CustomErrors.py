# Raising exceptions explicitly based on condition.

a = int(input("Enter a value between 0 to 10 : "))
if(a<0 or a>10):
    raise ValueError("Value b/w 0 and 10 needed")

# Defining Custom Exceptions - by creating new class that is derived from built-in exception class.
class CustomError(Exception):
    pass
