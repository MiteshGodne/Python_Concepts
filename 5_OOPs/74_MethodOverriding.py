# Method Overriding - Redefine parent class method in child class.
# It is used to customize methods according to needs.

class Shape:
    def __init__(self, x , y=0):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

# using parents method
class Rect(Shape):
    pass

rect = Rect(3,5)
print(rect.area())


# Overriding area() of parent in class
class Circle(Shape):
    # def __init__(self, r):
    #     return super().__init__(r,r)
    def area(self):
        return 3.14 * super().area()

circ = Circle(10)
print(circ.area())

