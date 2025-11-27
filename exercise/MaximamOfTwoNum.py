class Maximum:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def maximum(self):
        if self.a > self.b:
            print(self.a,"Maximum")
        else:
            print(self.b,"Maximum")

n = Maximum(2,3)
n.maximum()
