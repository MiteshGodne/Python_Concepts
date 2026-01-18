import time

# print("Time is : ", time.strftime(" %H : %M : %S of  %Y"))

# strftime : returns a time in string format 
hour = int(time.strftime("%H"))

if ( hour > 0 and hour < 12 ) :
    print("Good Morning")
elif (hour > 12 and hour < 17): 
    print("Good Evening")
else:
    print("Good Night")
