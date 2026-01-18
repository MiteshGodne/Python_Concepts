# Virtual Environment - 
'''
>>> It is a tool used to isolate specific Python Environment on a single machine, allowing us to work on multiple projects with different dependencies and packages and their versions to prevent conflicts between packages that does not support each other.
'''

# Commands -
''' 
-> venv module is used to create virtual env. & a folder is created with the specified name.
>>> python -m venv myEvtName 

-> activate virtual environment
>>> myEvtName\Scripts\activate.ps1 # for PowerShell
>>> myEvtName\Scripts\activate.bat # for cmd  

-> now we can install different packages with different versions
>>> pip install pandas==1.4.4

-> to deactivate activated virtual environment
>>> deactivate 

-> to delete virtual environment, simply delete the folder created
>>> rm -r myEvtName
''' 


# requirement.txt - file that contains packages and their versions required in the virtual environment
'''
1) displays all packages & versions
>>> pip freeze 

2) creates the requirements.txt file and adds all the packages and versions installed
>>> pip freeze > requirements.txt 

3) installs all the packages from requirements.txt file
>>> pip install -r requirements.txt 
'''