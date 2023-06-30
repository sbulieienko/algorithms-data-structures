zahl = input()

if len(zahl) == 4:
    if zahl[0] == zahl[-1] and zahl[1] == zahl[-2]:
        print('YES')
    else:
        print('NO')
else:
    print('Incorrect input, enter 4 digit number')
