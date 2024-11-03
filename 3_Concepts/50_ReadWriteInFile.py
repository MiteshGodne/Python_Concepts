# Writing into a file
""" 
>>> obj.write("string") - writes string to the file 
>>> obj.writelines(list) - writes string from list as lines to the file
NOTE - data is not written until file is closed.
NOTE - new line is not added until \n is not used.
"""
fileObj = open("VishnuStuti.txt", "w")
fileObj.write("Jay Sri Krishna")
l = ["\nJay", "\nSri", "\nRam"]
fileObj.writelines(l)
fileObj.close()

# Reading from a file 
"""
>>> read() - to read all file as string
>>> read(n) - to read specific number of bytes or "n" characters 
>>> readline() - to read only one line (reads until new line or EOL)
>>> readlines() - to read all the lines as list
"""
fileObj = open("VishnuStuti.txt","r")
data = fileObj.read()
print(data)

data2 = fileObj.read(4)
print(data2)

# NOTE - loop is generally used to read line by line
data3 = fileObj.readline()
print(data3)

data4 = fileObj.readlines()
print(data4)