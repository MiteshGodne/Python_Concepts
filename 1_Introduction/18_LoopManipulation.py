''' Jump Statements -'''
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


''' else statement with loop - Else part acts as the last iteration of the loop hence it is executed when the loop iterations are completed & therefore Loop ends when else part is executed'''

# else with for loop ->>
# NOTE - If loop break at certain point then else part does not get executed. 
for i in range(6):
    if(i==3):
        break
    print(i)
else:
    print("numbers printed") 
    
    
# else with while loop ->>
# NOTE - else part is executed only when while condition gets False at first check or if all iterations are completed,If loop break at certain point then else part does not get executed.
i = 0
while(i<5):
    if(i==3):
        break
    print(i)
    i+=1
else:
    print("Loop could not execute as condition is False")
    