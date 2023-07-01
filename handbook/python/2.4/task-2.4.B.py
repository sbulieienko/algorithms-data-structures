n = int(input())

for x in range(1, n + 1):
    for y in range(1, n + 1):
        mult = x * y
        print(f'{y} * {x} = {mult}')
