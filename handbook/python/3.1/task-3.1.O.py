def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


line = input()
items = line.split()

nod = int(items[0])

for item in items:
    nod = gcd(nod, int(item))

print(nod)    
