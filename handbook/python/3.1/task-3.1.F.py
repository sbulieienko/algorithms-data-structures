n = int(input())

lands = []

for _ in range(n):
    lands.append(input())

count1 = 0

for land in lands:
    land_list = land.split()
    for item in land_list:
        if item == 'зайка':
            count1 += 1

print(count1)

