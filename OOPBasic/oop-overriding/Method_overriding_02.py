class Shape:
    def execute(self):
         print('Shape execute Method')
         self.area()

    def area(self):
         print('Shape area Method')


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        rectangle_area = self.width * self.height
        print ('Rectangle area ',rectangle_area)
        return rectangle_area
class Circle(Shape):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.radius * self.radius * self.PI
        print ('Circle area ',circle_area)
        return circle_area

class Test(Shape):
    def __init__(self, radius):
        pass

r = Rectangle(100, 200)
r.execute()

c = Circle(1)
c.execute()

t = Test(1)
t.execute()