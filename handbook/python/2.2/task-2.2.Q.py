a = float(input())
b = float(input())
c = float(input())

if a == 0.0 and b == 0.0 and c == 0.0:
    print('Infinite solutions')
    quit()

D = b * b - 4 * a * c

if D < 0:
    print('No solution')
elif a == 0.0 and b == 0.0 and c != 0.0:
    print('No solution')
elif a == 0.0 and b != 0.0:
    x = (-1) * c / b
    print(f'{round(x, 2):.2f}')
elif D == 0.0 and a != 0.0:
    x = (-1) * b / (2 * a)
    print(f'{round(x, 2):.2f}')
else:
    if a == 0.0:
        x1 = ((-1) * c / a) ** (0.5)
        x1 = (-1) * ((-1) * c / a) ** (0.5)
    else:
        x1 = ((-1) * b + D ** (0.5)) / (2 * a)
        x2 = ((-1) * b - D ** (0.5)) / (2 * a)
    if x1 <= x2:
        print(f'{round(x1, 2):.2f}', f'{round(x2, 2):.2f}')
    else:
        print(f'{round(x2, 2):.2f}', f'{round(x1, 2):.2f}')
