import datetime

today = datetime.date.today()

formated = today.strftime("%d-%m-%Y")
print("Today's Date:", today)
print("Formatted Date:", formated)