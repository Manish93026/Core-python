# a=10
# b=1
#
# try:
#     c = a/b
#     print('divition',c)
#
# except ZeroDivisionError as e:
#     print('division by zero')
# else:
#     print('else block executed')
# finally:
#     print('in finally block')




a = 10
b = 2

try:
    # Code jisme error aasakta hai
    c = a / b
    print('division:', c)
except ZeroDivisionError as e:
    # Error aane par ye chalega
    print('exception:', e)
else:
    # Jab try me koi error NA aaye to ye chalega
    print('else block executed')
finally:
    # Chahe error aaye ya nahi, ye hamesha chalega
    print('finally block executed')




# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File nahi mili")
# else:
#     print("File successfully read")
# finally:
#     print("Cleanup complete")  # ✅ ye hamesha chalega






# try:
#     num = int(input("Enter a number: "))
#     print("Square is:", num * num)
# except ValueError:
#     print("Please number hi daalna tha")
# finally:
#     print("Program end")  # ✅ Always