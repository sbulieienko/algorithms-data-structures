N = int(input())
M = int(input())

n = 0
weite = len(str(N * M))

while n < N:
    row = ''
    n += 1
    for i in range(M):
        if row == '':
            row = str(n).rjust(weite)
        else:
            row += ' ' + str(n + i * N).rjust(weite)
    print(row)
