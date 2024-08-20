# Taking Input from the user -
 
# => input() is used to take input from the user which acts as raw_input() function of Python 2
a = input()
print(a)

# => string can be used inside the parenthesis to print on the output before taking the input.
name = input("Enter your name : ")
print(name)

# => Python by default takes input as string hence all other type of data is treated as string only.
x = input("Enter num : ")
print(type(x))

# => Type casting can be done while taking input to get input in other data type
y = int(input("Enter num : "))
print(type(y))

# => Multiple value input :  
# Takes multiple inout with by default delimiter as space
x,y = input().split()   # x and y are strings as input takes str type.
print(x+y)

# To convert into int, list comprehension is used : add int(x) 
a,b= [int(x) for x in input("Enter 2 numbers with space b/w them :").split()]
print("Product is :", a*b)
# split() takes whitespace as a separator by default.

# => eval() : can also be used to take string and process it directly as it evaluates the expression
res = eval(input("Enter the expression"))
print(res)


