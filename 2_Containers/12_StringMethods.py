a = "Abeer!!!   "
# String Methods - returns new string as strings are immutable 

# 1] a.upper() / a.lower 

# 2] a.swapcase() => changes uppercase to lowercase and vise versa
print(a.swapcase())

# 3] a.rstrip(char) => removes all continuous trailing chars / spaces
print(a.rstrip("!"))
print(a.rstrip())   # default " "

# 3] a.strip()=> removes whitespaces from beginning or the end

# 4] a.replace("old","new") => replaces all occurrences of old with new
print(a.replace("Ab", "B"))

# 5] a.split("separator") => returns a list that has string parts splitted by the separator passed  
list = a.split(" ")
print(list)

# ] a=separator.join(list / tuple)

# 6] a.capitalize() => turns only 1st character capital and others are converted to lowercase

# 7] a.center(int) =>  align string to the center by adding space equal to the parameter passed and the length becomes the parameter passed
print(a.center(20))

# 8] a.count(element) => count the no. of occurrences of a character/ substring in the string 
print(a.count("e"))

# 9] a.endswith("str") / a.startswith("str") => returns true if string ends/starts with specified chars. 
print(a.endswith("!"))
print(a.startswith("!"))
# it can be used with the part of a string
print(a.endswith("r", 0, 4))
print(a.startswith("A", 0, 4))

# 10] a.find("str", 'startIdx', 'stopIdx') => returns index of the 1st occurrence of the value passed and -1 if not present
print(a.find("z"))

# 11] a.index("str") => similar to find but it generates Value Error : Substring not found, if not found. 

# 12] a.isalnum() => returns True only if the whole string consists of only alpha-numerics 
print(a.isalnum()) 

# 13] a.isalpha() => returns True only if the whole string consists of only alphabets 
print(a.isalpha()) 

# 14] a.islower() / a.isupper => returns True if all characters are in lowercase / uppercase

# 15] a.isprintable() => returns True if all the values within strings are printable {Non printable characters such as '\n' }
print(a.isprintable())

# 16] a.isspace() => returns True only & only if whole string just contains white spaces.
print(a.isspace())

# 17] a.istitle() => returns True if all 1st letters of every word in the string is capital
print(a.istitle())

# 18] a.title() => converts every letter in 1st word of the string to uppercase 
print(a.title())

# 19] zfill() => fills string with (length - value_passed) number of 0s 
print(a.zfill(15))