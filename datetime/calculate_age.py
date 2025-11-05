import datetime

dob = datetime.date(2005,5,17)
today = datetime.date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Age is:", age)