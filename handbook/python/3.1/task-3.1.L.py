days = int(input())

cereals = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

i = 0

while days > 0:
    print(cereals[i])
    i += 1
    if i >= len(cereals):
        i = 0
    days -= 1
    