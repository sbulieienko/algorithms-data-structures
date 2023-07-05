N = int(input())
M = int(input())

n = 0
last = N * M
width = len(str(last))

for i in range(N):
    row = []
    for j in range(M):
        n += 1
        row.append(n)

    if i % 2 != 0:
        row = row[len(row)::-1]
    
    line = ''

    for i in row:
        if line == '':
            line = str(i).rjust(width)
        else:
            line += ' ' + str(i).rjust(width)

    print(line)
