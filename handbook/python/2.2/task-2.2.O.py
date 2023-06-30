a = input()
b = input()

max_digit = max(int(a[0]), int(a[1]), int(b[0]), int(b[1]))
min_digit = min(int(a[0]), int(a[1]), int(b[0]), int(b[1]))

min_char = 'null'
max_char = 'null'

ab = a + b
other_digits = ''

for i in range(0, 4):
    char_i = int(ab[i])
    if char_i == max_digit and max_char == 'null':
        max_char = str(char_i)
    elif char_i == min_digit and min_char == 'null':
        min_char = str(char_i)
    else:
        other_digits += str(char_i)

mid_digit = str(int(other_digits[0]) + int(other_digits[1]))[-1]

print(str(max_digit) + mid_digit + str(min_digit))
