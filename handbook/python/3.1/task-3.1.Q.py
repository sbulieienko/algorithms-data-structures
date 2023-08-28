satz = input()

direct = ''
reverse = ''

for char in satz:
    if char != ' ':
        direct = direct + char.lower()
        reverse = char.lower() + reverse

if direct == reverse:
    print('YES')
else:
    print('NO')