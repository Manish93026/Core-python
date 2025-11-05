import datetime

my_date = datetime.date(2005, 5, 17)

formated_date = my_date.strftime("%d-%m-%Y")
print("My brithday is:", formated_date)
