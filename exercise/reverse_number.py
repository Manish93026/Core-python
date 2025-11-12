num = 176

n = num
rem = 0
sum = 0

while n > 0:
    rem = n % 10
    sum = (sum * 10) + rem
    n = n // 10
print("The reverse of the number is:", sum)