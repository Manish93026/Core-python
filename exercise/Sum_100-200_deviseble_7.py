def Sum(n: int) -> int:
    total = 0
    for i in range(100, 200):
        if i % n == 0:
            total += i
    print('The sum is:', total)
    return total

# Example call
Sum(7)  # sums all numbers between 100 and 199 divisible by 7
