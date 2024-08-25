'''Conditional statements helps to execute statements based on certain conditions
1] if 
2] if else
3] if elif else
# You can nest if-else in python
4] match case -> comes with Python 3.10 
'''

# # if-elif-else
# a = int(input("Enter your age : "))
# if(a>18):
#     print("You can drive !!")
# elif(a==18):
#     print("You should learn driving")
# else:
#     print("You cannot drive !!")


# match-case - introduced in Python 3.7
# => It does not need break compulsorily.
# => if-else can be nested in a match case
# => It has _ as default case which can be used k/a irrefutable case.
# => more than one default case can be used only when if statement is used along with the default case
x = 21
a = "mon"
match a:
    case 'mon' if(x==21):
        print("Hello Abeer")
        print("Weekday")
    case 'tue':
        print("Weekday")
    case 'wed':
        print("Weekday")
    case 'thurs':
        print("Weekday")
    case 'fri':
        print("Weekday")
    case 6:
        print("Weekend")
    case 7:
        print("Weekend")
    case _ if(a==2): 
        print("Default Case 2")
    case _ if(a==13): 
        print("Default Case 13")
    case _ if(a==12): 
        print("Default Case 12")
    case _ if(a==15): 
        print("Default Case 15")
    case _ if(a==19): 
        print("Default Case 19")

