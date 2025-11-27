a=10
b=0

try:
    c = a/b
    print('divition',c)

except ZeroDivisionError as e:
    print('division by zero')
finally:
    print('in finally block')