num = 131

n = num

rem = 0
sum = 0

while n > 0:
    rem = n % 10
    sum = (sum * 10) + rem
    n = n // 10

if sum == num:
    print("This is palindrome number", num)
else:
    print("This is not palindrome number")