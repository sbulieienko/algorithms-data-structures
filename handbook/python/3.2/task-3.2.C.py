N = int(input())

lands = list()

for _ in range(N):
    lands.append(input())

set1 = set()

for land in lands:
    set2 = set(land.split())
    set1 = set1 | set2

for item in set1:
    print(item)
 