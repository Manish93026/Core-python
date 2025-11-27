class Fact:
    def __init__(self, n):
        self.n = n

    def fact(self):
        f = 1
        for i in range(1, self.n + 1):
            f = f * i
        print("The factorial of " + str(self.n) + " is " + str(f))

p = Fact(5)
p.fact()
