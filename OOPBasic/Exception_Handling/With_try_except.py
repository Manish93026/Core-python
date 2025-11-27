print('Before')

a=20
b=0

print('Mid')

try:
    c = a/b
    print('devition is: ',c)
except ZeroDivisionError as e:
    print('division by zero',e)
print('After')