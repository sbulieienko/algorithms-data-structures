n = int(input())

for x in range(1, n + 1):
    row = ''
    for y in range(1, n + 1):
        row = row + ' ' + str(x * y)
    print(row.strip())

    