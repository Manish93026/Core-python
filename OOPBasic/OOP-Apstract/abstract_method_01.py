from abc import ABC, abstractmethod


class Shape(ABC):
    def execute(self):
        self.area()

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        rectangle_area = self.width * self.height
        print('Area of rectangle is: ',rectangle_area)
        return rectangle_area

r = Rectangle(10, 20)
r.execute()

# Polymorphism: Shape type reference holding Rectangle object

shape: Shape = Rectangle(5,20)
shape.execute()
