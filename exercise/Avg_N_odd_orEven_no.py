avg_even = 0
avg2 = 0


for i in range(1,20):
    if  i % 2 == 0:
        avg_even = avg_even + i

    else:
        avg2 = avg2 + i

print("the average of even no. is: ",avg_even)
print("the average of odd no. is: ",avg2)