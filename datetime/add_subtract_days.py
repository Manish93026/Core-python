import datetime

today = datetime.date.today()
future = today + datetime.timedelta(days=7)
past = today - datetime.timedelta(days=7)

formated_future = future.strftime("%d-%m-%Y")
formated_past = past.strftime("%d-%m-%Y")
print("7 days later:", formated_future)
print("7 days ago:", formated_past)
print(today)