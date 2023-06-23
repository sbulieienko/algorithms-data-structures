product = input()
price = int(input()) 
weight = int(input())
money = int(input())

cost = price * weight
ret = money - cost

gewicht = str(weight)
preis = str(price)
kost = str(cost)
geld = str(money)
zuruk = str(ret)

print('================Чек================')

print('Товар:' + ' ' * (35 - 6 - len(product)) + product)

print('Цена:' + ' ' * (35 - 16 - len(gewicht) - len(preis)) + gewicht + 'кг' + ' * ' + preis + 'руб/кг')

print('Итого:' + ' ' * (35 - 9 - len(kost)) + kost + 'руб')

print('Внесено:' + ' ' * (35 - 11 - len(geld)) + geld + 'руб')

print('Сдача:' + ' ' * (35 - 9 - len(zuruk)) + zuruk + 'руб')

print('===================================')