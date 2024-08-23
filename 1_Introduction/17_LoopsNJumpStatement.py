''' for loop - iterates over a sequence of iterable objects such as string, list, tuple, set, range() that returns no. sequence, etc.  
'''

# for loop - with string
name = " Abeer "  
for char in name:
    print(char,end=",")
print()

# for loop - with list
list1 = [1,2,3,4]
sum = 0
for i in list1:
    sum = sum + i
print("Sum is",sum)

# for loop - with range() 
# range() returns a sequence of numbers from 0 to value-1  
# range() takes 3 parameters separated by comma => range(start,stop,step)
# start -> index from where the number sequence starts (by default 0)
# stop -> index before which the number sequence stops {stop is exclusive}
# step -> increment/decrement between the number sequence
for i in range(10,1,-2):
    print(i, end=" ")


print()



'''while loop - especially convenient when number of iterations are not known and it runs till we have condition as True'''

# update statement is required inside the loop 
j = 0
while(j<5):
    print(j, end=" ")
    j+=1


print()

# else with while loop can be used 
j = 10
while(j<0):
    print(i)
else:
    print("Loop could not execute as condition is False")


# break - It is used to break the loop in which it is present
for i in range(15):
    if(i==10):
        break
    else:
        print(i+1)


# continue - It is used to skip the current iteration of the loop 
for i in range(11):
    if(i%2==0):
        continue
    else:
        print(i)
    
# we can emulate do while loop in python by creating an infinite while loop with a break


'''do while loop - Python does not support do while loop which executes once irrespective of condition is met or not'''
# We can emulate do while loop using while loop and break
while True:
    n = int(input("Enter a +ive number "))
    print(n)
    if not n>0:
        print("Loop end as num entered is -ve")
        break