n = int(input())

lands = []

for _ in range(n):
    lands.append(input())

for land in lands:
    try:
        indx = land.index('зайка')
        print(indx + 1)
    except Exception:
        print('Заек нет =(')
