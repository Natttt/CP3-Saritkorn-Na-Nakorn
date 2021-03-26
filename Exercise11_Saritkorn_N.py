row = int(input("Enter Number of rows : "))
for x in range(row):
    print(" " * (row - x), "*" * (((x + 1) * 2) - 1))
print("Total Rows :", row)
