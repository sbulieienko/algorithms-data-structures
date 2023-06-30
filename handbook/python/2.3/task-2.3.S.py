small = 1
big = 1001
inp = None

while inp != 'Угадал!':
    ans = (small + big) // 2
    print(ans)
    inp = input()
    if inp == 'Больше':
        small = ans
    elif inp == 'Меньше':
        big = ans
