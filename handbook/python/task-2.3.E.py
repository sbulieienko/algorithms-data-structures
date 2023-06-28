sum = 0.0
price = None

while price != 0:
    price = float(input())
    if price >= 500:
        price = price * 0.9
    sum += price

print(sum)

