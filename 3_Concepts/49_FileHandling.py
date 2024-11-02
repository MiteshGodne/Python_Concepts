'''
=> Text and Binary File stores data permanently.
=> Text files can be :-
>>> Regular Text Files  - .txt extension
>>> Comma separated value (CSV) Files  = .csv extension
=> Binary files stores data in the form of stream of bytes used to store images, videos and audio data.
'''

# Opening a file -
file_obj = open("VishnuStuti.txt", "x+t")

#  Modes of File -
'''
Mode   Meaning
'r'	   open for reading (default) else FileNotFoundError
'w'	   open for writing, truncating it first else create new file
'a'	   appending to end of file if it exists else create new file
'x'	   create new file & open it in exclusive creation write mode
'+'	   open a disk file for updating (reading and writing)
NOTE - suffix every mode with b for binary files such as jpg, image files, audio, exe, etc files.
'''

# Properties of File Object - 
'''
>>> name : Name of opened file
>>> mode : Mode in which the file is opened
>>> closed : Returns True/False if file is closed or not
>>> readable(): Returns True/False if file is readable or not
>>> writable(): Returns True/False if file is writable or not.
'''

# Closing a file - To free up resources. 
file_obj.close()




# writelines adds iterable object one by one to file
truncate()