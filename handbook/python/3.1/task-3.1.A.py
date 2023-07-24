n = int(input())

for _ in range(n):
    str1 = input()
    if str1[0] not in list('АБВабв'):
        print('NO')
        exit()

print('YES')