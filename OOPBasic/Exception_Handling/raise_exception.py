
try:
    number = int(input("Enter your Number:"))

    #Yaha par hum apne hisab se exception bana sakte h
    if number > 10:
        raise Exception('invalid number')
except Exception as e:
    print('exception:', e)

print('after')