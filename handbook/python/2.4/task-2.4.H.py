n = int(input())

biggest = None
winner_name = None

for i in range(n):
    name = input()
    zahl = input()
    sum1 = 0

    for j in zahl:
        sum1 += int(j)
    
    if biggest is None:
        biggest = sum1
        winner_name = name
    elif biggest <= sum1:
        biggest = sum1
        winner_name = name

print(winner_name)        