a,b,c = 1,0,0
for i in range(50):
    print(c, end=" ")
    c = a+b
    a,b = b,c