'''
>>> The OrderedDict is a dictionary subclass that explicitly remembers the order in which items were inserted. 
>>> OrderedDict provides additional functionality for order manipulation such as move_to_end() & pop_item(last=false) -> FIFO support.
>>> Difference from dict - Order-Sensitive Equality: Two OrderedDict objects are considered equal only if their items are equal and in the same order. Standard dict equality ignores order. Standard dict does not provide FIFO support.
>>> Time Complexity : Creation->O(n), Others->O(1)
'''

'''Example'''
from collections import OrderedDict

# 1. Initialization
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3

# 2. move_to_end(key, last=True)
# Move 'first' to the very end
od.move_to_end('first') 
# Order: second, third, first

# Move 'second' to the very beginning (last=False)
od.move_to_end('second', last=False) 
# Order: second, third, first -> second is already first, but if it were in middle:
# Result: second, third, first

# 3. popitem(last=True/False)
# LIFO: Remove last item (default behavior like standard dict)
last_item = od.popitem() 
print(last_item)  # Output: ('first', 1)

# FIFO: Remove FIRST item (Queue behavior - unique to Orde   