n = int(input())

lines = list()
line_items = 1
last_width = 0
i = 1

while i < n + 1:
    line = list()
    for _ in range(line_items):
        line.append(str(i))
        i += 1
        if i > n:
            break
    lines.append(line)
    line_items += 1
    width = len(' '.join(line))
    if width > last_width:
        last_width = width


for line in lines:
    str1 = ' '.join(line)
    left = ' ' * ((last_width - len(str1)) // 2)
    print(left + str1)