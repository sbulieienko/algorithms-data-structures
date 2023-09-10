N = int(input())
M = int(input())

manka = set()

for _ in range(N):
    manka.add(input())

ovsyanka = set()

for _ in range(M):
    ovsyanka.add(input())

both = manka & ovsyanka

n = len(both)

if n == 0:
    print('Таких нет')
else:
    print(n)