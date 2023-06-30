product = input()
price = int(input()) 
weight = int(input())
money = int(input())

print('Чек')
print(f"{product} - {weight}кг - {price}руб/кг")

cost = price * weight
print(f"Итого: {cost}руб")
print(f"Внесено: {money}руб")

zuruk = int(money - cost)

print(f"Сдача: {zuruk}руб")