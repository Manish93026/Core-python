class Shape:

    def __init__(self):
        self.color=''
        self.boderWidth = 0

    def set_color(self,c):
        self.color = c

    def get_color(self):
        return self.color

    def set_borderWidth(self,bw):
        self.boderWidth = bw

    def get_boderWidth(self):
        return self.boderWidth

s = Shape()
s.set_color('Red')
s.set_borderWidth(2)
print("Color:",s.get_color())
print("Border Width:",s.get_boderWidth())