x = 0
y = 0
richtung = None

while True:
    richtung = input()
    if richtung == 'СТОП':
        break
    i = int(input())
    if richtung == 'СЕВЕР':
        y += i
    elif richtung == 'ВОСТОК':
        x += i
    elif richtung == 'ЮГ':
        y -= i
    elif richtung == 'ЗАПАД':
        x -= i

print(y)
print(x)