# Initialize 2D array for tables from 2 to 10
tables = []
for i in range(2, 11):        # Rows: 2 to 10
    row = []
    for j in range(1, 11):    # Columns: 1 to 10
        row.append(i * j)
    tables.append(row)

# Display the tables neatly
for i, row in enumerate(tables, start=2):
    print(f"Table of {i}: ", end="")
    for value in row:
        print(value, end="\t")
    print()
