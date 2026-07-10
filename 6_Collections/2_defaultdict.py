'''
defaultdict()
A dictionary subclass that calls a factory function to supply missing values. It never raises a KeyError even if key is not present opposite to the standard dictionary.
'''

'''Example'''
from collections import defaultdict

# 1. Initialization with factory functions
# int() returns 0, list() returns [], lambda returns custom values
counts = defaultdict(int) 
groups = defaultdict(list)
custom = defaultdict(lambda: "Not Found")

# 2. Automatic Initialization (No KeyError)
counts["apple"] += 1  # Automatically creates 'apple' with value 0, then adds 1
groups["fruits"].append("banana") # Automatically creates 'fruits' with empty list

# 3. Accessing missing keys
print(custom["missing_key"])  # Output: "Not Found" (instead of raising KeyError)

# 4. Common Pattern: Counting
data = ["a", "b", "a", "c", "b", "a"]
for item in data:
    counts[item] += 1
print(dict(counts))  # Output: {'a': 3, 'b': 2, 'c': 1}   