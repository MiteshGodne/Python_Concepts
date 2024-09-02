# Enumerate Function -
'''
-> Built-in function that allows us to loop over a sequence (list, tuple, string) and access the  index and value of each element in the sequence at the same time without creating another variable and update it.
-> enumerate() returns the enumerate object that contains every index and value in a different tuple. '''

marks = [12,34,55,78,33,98]
value = enumerate(marks)
print(type(value))    # <class enumerate>
for i in value:
    print(i)  # i = (idx,value) for every iteration
    
    
# Using Tuple Unpacking inside the loop syntax :- 
for index,mark in enumerate(marks):
    if(index==3):
        print(mark)
        

# NOTE - enumerate(iterable, start) - start index can also be passed which changes the starting index value from 0 to start_idx, hence changing the index values to the specified start_idx.
for idx, mark in enumerate(marks, start = 4):
    print(idx, mark)
    
