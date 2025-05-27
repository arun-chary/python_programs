from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius**2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# You cannot create an instance of an abstract class directly:
# shape = Shape() # This would raise a TypeError

rect = Rectangle(5, 10)
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

circ = Circle(7)
print(f"Circle Area: {circ.area()}")
print(f"Circle Perimeter: {circ.perimeter()}")
