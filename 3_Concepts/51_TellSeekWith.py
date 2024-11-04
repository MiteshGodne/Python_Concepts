# with statement 
'''
>>> We can use with to group file operation statements within a block.
>>> It will take care closing of file, after completing all operations automatically even in the case of exceptions also.'''

with open("VishnuStuti.txt", "r") as fileObj:
    print(fileObj.read())


# tell() - It is a method that returns current position of the file pointer according to the 0 base indexing.
with open("VishnuStuti.txt", "r") as fileObj:
    print(fileObj.readline())
    print(fileObj.tell())

# seek(offset, startingIdx) - It is a method used to move cursor(file pointer) to specified location in file.
'''
offset : represents the number of positions.
Starting index : 0---> From beginning of file.

NOTE - Deprecated with Python2 
1---> From current position
2---> From end of the file
'''
with open("VishnuStuti.txt", "r") as fileObj:
    print(fileObj.seek(4))
    print(fileObj.read())
    
    
# truncate(byteSize) - It reduces the size of file to the number of characters given and remove remaining data.
# NOTE- It works when file is opened in "w" or "a" mode. only. And any data written previously converts to Null.
with open("VishnuStuti.txt", "w") as fileObj:
    fileObj.write("Jay sri ram")
    fileObj.truncate(6)