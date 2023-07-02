n = int(input())

print('А Б В')

for i in range(1, n + 1):
    for j in range(1, n - 1):
        for k in range(n - 2, 0, -1):
            if i + j + k == n:
                print(f'{i} {j} {k}')



