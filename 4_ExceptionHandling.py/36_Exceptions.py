# Exception Handling - Used to handle run time errors.
# NOTE- Standard exception names are built-in identifiers (not reserved keywords) hence can be used as variable names

'''
try:
    // code
except ExceptionClass as ObjName:
    // code to execute if error occurred
except: 
    // general error message for all
else:
    // runs only if error doesn't occur
finally: 
    // runs always & used to clean resources and close objects
'''

a,b=10,0
try:
    print(a/b)
    print("Error might occur") #skipped
except ZeroDivisionError:
    print("Cannot divide by 0")
except NameError as n:
    n.add_note("This is name error")
    arguments = n.args
    print(n)
    raise 
except Exception as e:
    print(e)
except (RuntimeError, TypeError, NameError):
    print("Multiple Types together in tuple form")
except:
    print("Some Error Occurred")
else:
    print("No Error occurred")
finally:
    print("Resources Freed, Object closed")
print("Program Executed Successfully")
    

# finally will be the last to execute -
# even if function returns, 
def bool_return():
    try:
        return True
    finally:
        return False
bool_return()   # False
# statement breaks / continues
# even if except / else clause throws another exception


# Predefined Cleanup Actions
'''
>>> When a objects like is opened code leaves the file open for an indeterminate amount of time after this part of the code has finished executing.
>>> The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.'''
# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")
        
        
# NOTE -  e.add_note("note") - function used to add info to the exception after it is caught
# NOTE - e.args - used to get the arguments passed during raise

# ExceptionGroup - used to catch multiple exceptions at the same time
''' 
try:

    exceptions = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup("Message", exceptions)
except* OSError as oe:
    print("OS Error")    
'''