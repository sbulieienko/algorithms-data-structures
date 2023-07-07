n = int(input())

for i in range(n):
    row = ''
    for j in range(n):
        d = min(i, j, n - i - 1, n - j - 1) + 1
        w = len(str((n + 1) // 2))
        if row == '':
            row = str(d).rjust(w)
        else:
            row += ' ' + str(d).rjust(w)
    
    print(row)

