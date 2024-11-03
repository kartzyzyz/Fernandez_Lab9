rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(' '.join(str((i * (i - 1)) // 2 + j + 1) for j in range(i)))