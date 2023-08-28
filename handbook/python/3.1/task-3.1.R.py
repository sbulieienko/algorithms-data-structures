items = input()

cur_item = items[0]
cur_sum = 0

for item in items:
    if item == cur_item:
        cur_sum += 1
    else:
        print(f'{cur_item} {cur_sum}')
        cur_item = item
        cur_sum = 1

print(f'{cur_item} {cur_sum}')

