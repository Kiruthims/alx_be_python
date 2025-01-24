import math

# Base Class - Shape
class Shape:
    def area(self):
        raise NotImplementedError("The area() method must be overridden in subclasses.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

