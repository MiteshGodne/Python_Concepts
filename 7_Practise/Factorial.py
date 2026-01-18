def factorial(num):
    for i in range(1,num):
        num = num*i
    return num
print(factorial(int(input("Enter a number : "))))

