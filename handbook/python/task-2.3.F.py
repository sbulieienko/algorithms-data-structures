a = int(input())
b = int(input())

if a >= b:
    big = a
    small = b
else:
    big = b
    small = a

r = None

while r != 0:
    r = big % small
    big = small
    small = r

print(big)
