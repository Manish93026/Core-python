number =152
n = number
sum = 0
rem = 0

while n > 0:
    rem = n % 10
    sum = sum + (rem * rem * rem)
    n = n // 10

if sum == number:
    print("This is  Armstrong number",number)
else:
    print("This is not Armstrong number")