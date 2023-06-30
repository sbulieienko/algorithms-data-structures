msg = input()

if len(msg) != 3:
    quit()

min_digit = min(int(msg[0]), int(msg[1]), int(msg[2]))
max_digit = max(int(msg[0]), int(msg[1]), int(msg[2]))

min_char = 'null'
max_char = 'null'

for i in range(0, 3):
    char_i = int(msg[i])
    if char_i == max_digit and max_char == 'null':
        max_char = str(char_i)
    elif char_i == min_digit and min_char == 'null':
        min_char = str(char_i)
    else:
        other = char_i

if (min_digit + max_digit) == other * 2:
    print('YES')
else:
    print('NO')


