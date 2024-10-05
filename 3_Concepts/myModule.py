def greet():
    print("Hello, Good Morning !!")
    
print("executed by :",__name__)  # returns filename from which it is executed
'''
>>> if 45__name__.py is executed it returns myModule, if
>>> if myModule.py is executed then it returns __main__
'''
if __name__ == "__main__":
    greet()
