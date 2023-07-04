N = int(input())
M = int(input())

n = 0
last = N * M
digits = len(str(last))

while n < last:
    row = ''
    for i in range(M):
        n += 1
        if row == '':
            row = str(n).rjust(digits)
        else:
            row += ' ' + str(n).rjust(digits)
    print(row)
