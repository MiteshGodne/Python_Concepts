'''The collections module in Python is a built-in library that provides specialized "container" data types. While standard types like list and dict are great for general tasks, collections offers tools optimized for specific backend challenges like memory efficiency, data counting, and high-speed data manipulation.
'''

''' 
>>> namedtuple (The Readable Tuple)
>>> A factory function for creating tuple subclasses with named fields. It turns a regular tuple into a lightweight, immutable object.The Logic: It creates a "mini-class" that doesn't allow the data to be changed (immutable) but lets you use names.

>>> Why use namedtuple?They use less memory compared to regular classes because they don't have per-instance dictionaries.
'''
from collections import namedtuple

# 1. Create the 'Blueprint' (The Class)
# We are naming the type 'User' and giving it two fields: 'name' and 'role'
User = namedtuple('User', ['name', 'role'])

# 2. Create the 'Instance' (The Object)
user1 = User(name="Alice", role="Admin")

# 3. Access the data
print(user1.name)  # Output: Alice
print(user1[0])    # Output: Alice (You can still use indexes!)