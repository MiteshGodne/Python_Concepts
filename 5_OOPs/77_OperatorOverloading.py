'''
>>> Operator Overloading - It is a feature in python that allows developers to redefine the behavior of operators for custom data types such as objects, functions, etc. Dunder methods are used and defined inside the class to perform operator overloading.

# These methods can be - 
>>> add(self, other): Overloads + 
>>> sub(self, other): Overloads - 
>>> mul(self, other): Overloads * 
>>> truediv(self, other): Overloads /
>>> floordiv(self, other): Overloads //
>>> and(self, other): Overloads &
>>> or(self, other): Overloads |
>>> xor(self, other): Overloads ^
>>> rshift(self, other): Overloads >>
>>> lshift(self, other): Overloads <<
>>> matmul(self, other): Overloads @
>>> mod(self, other): Overloads % 
>>> lt(self, other): Overloads < 
>>> le(self, other): Overloads <=
>>> eq(self, other): Overloads ==
>>> ne(self, other): Overloads != 
>>> gt(self, other): Overloads > 
>>> ge(self, other): Overloads >=
>>> divmod(self, other):  
>>> pow(self, other, [third parameter]):  
'''
class Vector:
    def __init__(self, i , j , k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
    
    def __sub__(self, other):
        # we can return the Vector type of data as arithmetic of vectors returns in vectors only.
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)    
v1 = Vector(3,5,6)
print(v1)
v2 = Vector(4,7,2)
print(v2)

# we can't operate v1 and v2 directly but if we can overload individual arithmetic/comparison operators using their specific dunder methods.
print(v1+v2)
print(v1-v2)
