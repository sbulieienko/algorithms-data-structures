zahl = input()

gros = int(zahl[0])

for i in zahl:
    if gros < int(i):
        gros = int(i)

print(gros)

