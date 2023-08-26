line = input()
pow = int(input())

items = line.split()

for i in range(len(items)):
    items[i] = str(int(items[i])**pow)

print(' '.join(items))    

