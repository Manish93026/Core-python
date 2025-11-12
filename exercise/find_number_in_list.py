list = [10, 11 ,52,45 ,78,90,100]
number = 78

count = 0

for i in list:
    if i == number:
        count += 1


if number in list:
    print("number exist")
else:
    print("number does not exist")