''' for loop - iterates over a sequence of iterable objects such as string, list, tuple, set, range() that returns no. sequence, etc.  
'''

# for loop - with string
name = " Abeer "  
for char in name:
    print(char,end=",")

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



'''while loop - especially convenient when number of iterations are not known and it runs till we have condition as True'''

# update statement is required inside the loop 
j = 0
while(j<5):
    print(j, end=" ")
    j+=1


'''do while loop - Python does not support do while loop which executes once irrespective of condition is met or not'''
# we can emulate do while loop in python by creating an infinite while loop with a break
while True:
    n = int(input("Enter a +ive number "))
    print(n)
    if not n>0:
        print("Loop end as num entered is -ve")
        break


    