n = int(input())
i = 1
count1 = 1

while i <= n:
    row = ''
    for j in range(count1):
        row += ' ' + str(i)
        i += 1
        if i > n:
            break
    count1 += 1
    print(row.strip())
