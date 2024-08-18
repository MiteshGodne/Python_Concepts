''' 
A] print() : used to print objects in output
->print function evaluates the expression written in the parenthesis (termed as REPL) and print them. 
->It is a function that takes objects as arguments.
->Multiple strings along with variables as well as sequence data types such as list and tuple can be printed using single print() function.
->Print functions returns None
'''


# print() without arguments prints new line.


# With Arguments : Positional(1) and Keyword(2,3,4,5) 
# => 1. *value to print (should be an object)
print("Hello Python")

# => 2. sep -> separator of multiple arguments | Default >> sep = " ",
print("Hello", "World", "Python", sep=" - ")

# => 3. end -> ending of the print function | Default >> end = "\n",
print("Hello", "World", "Python", end=None)

# => 4. flush -> used to clear internal output buffer | Default >> flush = "False"
print("Hello", "World", flush="True")

# => 5. file -> SupportsWrite[str] | Default >> file = "None",
myfile = open("Hello.txt", "w")
print("Hello", "World", file=myfile)



''' 
B] Escape Sequences Characters : characters that cannot be added into string.  '''
#It can be - 
# 1. \n -> to print line break
# 2. \" -> to print "
# 3. \\ -> to print backward slash
# 4. \t -> to print 3 spaces 



