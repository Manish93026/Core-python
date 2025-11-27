class Minimum:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def minimum(self):
        if self.a < self.b:
            print(self.a," is minimum")

        else:
            print(self.b," is maximum")

m = Minimum(2,3)
m.minimum()
