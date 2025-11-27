class Shape:
    def execute (self):
        if self.validate():
            self.area()
        else:
            print('Validation Failed')


    def validate(self):
        return False

    def area(self):
        print('Area of Shape')

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def validate(self):
        if self.height > 0 and self.width > 0:
            return True
        else:
            return False

    def area(self):
        rectangle_area = self.width * self.height
        print('Area of Rectangle',rectangle_area)
        return rectangle_area
class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def validate(self):
        if self.radius > 0:
            return True
        else:
            return False

    def area(self):
        circle_area = self.radius * self.radius * self.PI
        print('Area of Circle',circle_area)
        return circle_area


class Test(Shape):
    pass

print("----- Rectangle -----")
r = Rectangle(10,20)
r.execute()

print("----- circle -----")
c = Circle(5)
c.execute()

print("----- Invalid Rectangle -----")
r_invalid = Rectangle(-10,20)
r_invalid.execute()

print("----- Invalid circle -----")
c_invalid = Circle(5)
c_invalid.execute()

print("----- Test -----")
t = Test()
t.execute()