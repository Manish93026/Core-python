num = 11
count = 0

for i in range(2, num):
    if num % i == 0:
        count += 1
if count == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")