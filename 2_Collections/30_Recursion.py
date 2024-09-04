# Recursion - Means a defined function can call itself. 

def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5))


# '''>>> Print Fibonacci Series'''
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i), end=" ")

# '''>>> Store Fibonacci Series using List Comprehension'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
fib_list = [fibonacci(i) for i in range(10)]
print("\n",fib_list,sep="")


# '''>>> Store fibonacci series using append() method'''
def fibonacci(num,l = [0], a = 0, b = 1):
    if(b-a >= num):
        return l
    l.append(b)
    return fibonacci(num,l, b, a+b)
print(fibonacci(10))
