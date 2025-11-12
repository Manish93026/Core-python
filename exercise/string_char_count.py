str = "string char count"

count = 0

for char in str:
    if char == 'c':
        count += 1

print("The character 'c' appears", count, "times in the string.")