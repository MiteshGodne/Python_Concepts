'''
defaultdict()
A dictionary subclass that calls a factory function to supply missing values. It never raises a KeyError even if key is not present opposite to the standard dictionary.
'''

'''Example'''
from collections import defaultdict

# 'int' is the factory function; default value for int is 0
book_counts = defaultdict(int)

# No need to check if 'John' exists; it creates the key automatically
book_counts['John'] += 1

print(book_counts['John']) # Output: 1
print(book_counts['Sarah']) # Output: 0 (No KeyError!)