n = int(input())

if n == 1:
    print('NO')
    exit()

if n == 2:
    print('YES')
    exit()

for i in range(2, n // 2 + 1):
    if (n % i) == 0:
        print('NO')
        exit()

print('YES')
