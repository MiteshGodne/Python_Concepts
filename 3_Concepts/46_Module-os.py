# OS Module - 
''' 
>>> provides functions to interact with the operating system like creating files and directories, management of files and directories, input, output, environment variables, process management, etc.
>>> OS module has built-in classes, objects, methods and constants.
'''

import os
# to check if folder exists, do task on condition 
if(not os.path.exists("data")):   
    # to create a directory
    os.mkdir("data")     
    
# to perform an operation multiple times , use loop
if(os.path.exists("data")):
    for i in range(1,5):    
        os.mkdir(f"data/Day{i}")  

# to rename a directory from source to destination
if(os.path.exists("data")):
    os.rename("data", "OsModuleCommands")  

# returns list of all folders in a dir
print(os.listdir("OsModuleCommands"))

# to run a command 
os.system("python --version")

# returns current working directory
os.getcwd()

# to change the directory
# os.chdir("directory name")

# to remove a directory
os.remove("directory")

# to remove empty directory
os.rmdir("directory")
    
'''
>>> 
'''