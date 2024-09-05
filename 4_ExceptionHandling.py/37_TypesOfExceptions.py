# Exceptions are errors that occur at run time & they can be 

# NOTE - BaseException is base class of all exceptions in python 

# Fatal Exceptions - 
'''It is an unrecoverable error that causes the program to terminate immediately and not intended to be caught. 
>>> BaseException
    >>> SystemExit
    >>> KeyBoardInterrupt
    >>> MemoryError
'''


# Non-Fatal Exceptions -
'''It is an unrecoverable error that may not cause the program to terminate and are needed to be handled in the program. 
>>> BaseException
    >>> Exception 
        >>> Arithmetic Error
            ->> ZeroDivisionError
            ->> FloatingPointError
            ->> OverflowError
            
        >>> LookupError
            ->> IndexError
            ->> keyError
            
        >>> EnvironmentError
            ->> IOError
            ->> OSError
            
        >>> NameError
        
        >>> ValueError
        
        >>> TypeError
        
        >>> RuntimeError
'''