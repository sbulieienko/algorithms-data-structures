n = int(input())
biggest = ''

for i in range(n):
    zahl = input()
    big = None

    for j in zahl:
        if big is None:
            big = j
        elif int(big) < int(j):
            big = j

    biggest += big

print(biggest)
