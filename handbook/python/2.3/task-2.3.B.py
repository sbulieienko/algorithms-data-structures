counter1 = 0
msg = None

while msg != 'Приехали!':
    msg = input()
    if 'зайка' in msg:
        counter1 += 1

print(counter1)
