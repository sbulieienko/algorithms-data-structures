n = int(input())

ans = 0

for i in range(n):
    flag = False
    while (place := input()) != 'ВСЁ':
        if 'зайка' in place and not flag:
            ans += 1
            flag = True

print(ans)