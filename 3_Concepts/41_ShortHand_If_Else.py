# If-else ShortHand -> acts as Ternary Operator in Python 
# Each Operand is an expression but cannot be an assignment statement as it gives syntax error
# Syntax - true_value if condition else false_value
# true & false values are compulsory. 
# elif cannot be used here.


a,b = 10,20
print(a) if a>b else print(b) # O/p -> 0


# Nested if-else ShortHand -> 
print(a) if a>b else print(f"{a}={b}") if a == b else print(b)

