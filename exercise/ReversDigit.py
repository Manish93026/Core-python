class ReversDigit:
    def __init__(self, num):
        self.number = num

    def reverse(self):
        self.number %= 10
        return self.number
