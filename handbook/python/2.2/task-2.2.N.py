mag = input()

if len(mag) != 3:
    quit()

min_digit = min(int(mag[0]), int(mag[1]), int(mag[2]))
max_digit = max(int(mag[0]), int(mag[1]), int(mag[2]))

min_char = 'null'
max_char = 'null'

for i in range(0, 3):
    char_i = int(mag[i])
    if char_i == max_digit and max_char == 'null':
        max_char = str(char_i)
    elif char_i == min_digit and min_char == 'null':
        min_char = str(char_i)
    else:
        other_digit = char_i

if min_digit == 0:
    print(str(other_digit) + str(min_digit), str(max_digit) + str(other_digit))
else:
    print(str(min_digit) + str(other_digit), str(max_digit) + str(other_digit))
