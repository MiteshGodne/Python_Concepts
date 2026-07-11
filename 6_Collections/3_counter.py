'''
>>> Dictionary subclass specifically designed for counting hashable objects (like items in a list or characters in a string).
>>> It stores elements as dictionary keys and their counts as dictionary values. 
>>> Time Complexity : Creation -> O(n), Others -> O(1)'''

from collections import Counter

# 1. Initialization from iterable
data = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(data)

# 2. most_common(n) - Get top N frequent items
print(counts.most_common(2))  # Output: [('apple', 3), ('banana', 2)]
print(counts.most_common(1))  # Output: [('apple', 3)]

# 3. Arithmetic Operations (Union, Intersection, Add, Subtract)
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=1)

print(c1 + c2)   # Addition: Counter({'a': 4, 'b': 3, 'c': 1})
print(c1 - c2)   # Subtraction (only positive results): Counter({'a': 2})
print(c1 & c2)   # Intersection (min counts): Counter({'a': 1, 'b': 1})
print(c1 | c2)   # Union (max counts): Counter({'a': 3, 'b': 2, 'c': 1})

# 4. Missing keys return 0
print(counts["grape"])  # Output: 0 (No KeyError)

# 5. Update and Subtract
counts.update(["grape", "grape"]) # Adds counts
counts.subtract(["apple"])        # Subtracts counts