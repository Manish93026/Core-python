import datetime

D=datetime.date.today()

print(D)
print(D.year)
print(D.month)
print(D.min)
formated = D.strftime("%d-%m-%Y")
print(formated)
