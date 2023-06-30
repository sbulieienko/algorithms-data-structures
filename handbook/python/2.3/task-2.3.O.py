n = int(input())

sum = 0

for i in range(n):
    msg = input()
    if 'зайка' in msg:
        sum += 1

print(sum)
