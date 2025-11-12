number = [10, 11, 52, 45, 78, 90, 100]
hightest = 0
second_hightest = 0

for num in number:
    if num > hightest:
        second_hightest = hightest
        hightest = num
    elif num > second_hightest and num != hightest:
        second_hightest = num

print("The largest number is:", hightest)
print("The second largest number is:", second_hightest)