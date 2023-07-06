def drucken(line, w):
    row = ''
    for x in line:
        if row == '':
            row += str(x).rjust(w)
        else:
            row += ' ' + str(x).rjust(w)
    print(row)


rows = int(input())
columns = int(input())
w = len(str(rows * columns))

for i in range(1, rows + 1):
    line = []
    for j in range(1, columns + 1):
        if j % 2 == 0:
            n = j * rows - i + 1
        else:
            n = i + (j - 1) * rows 
        line.append(n)
    drucken(line, w)
