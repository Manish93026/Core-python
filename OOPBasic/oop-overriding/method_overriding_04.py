
from typing import List


class Shape:

    def area(self):
        print('Shape Area Method')



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print('Rectangle Area:', rectangle_area)
        return rectangle_area



class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print('Circle Area:', circle_area)
        return circle_area



shapes: List[Shape] = [
    Rectangle(5, 10),
    Circle(7)
]


for shape in shapes:
    shape.area()

shape: Shape = Rectangle(10, 20)
shape.area()