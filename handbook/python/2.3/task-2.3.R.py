n = int(input())
div = 2
i = n // 2 + 1
ans = ''

while div <= i:
    while True:
        if n % div == 0:
            n = n / div
            if ans == '':
                ans = str(div)
            else:
                ans = ans + ' * ' + str(div)
        else:
            break
    div += 1

print(ans)


