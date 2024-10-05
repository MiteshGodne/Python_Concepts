'''
>>> just by import module command, the whole module is executed and if the module contains function call or object creation etc, they all are executed.
>>> to prevent automatic execution of a module while import, add a condition if __name__ == reqFileName
>>> __name__ returns the current file name which had executed it.
'''

import myModule 

print(__name__) # returns __main__ if 45__name__.py is run else 45__name__.py if it is executed by any other module

