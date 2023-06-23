N = int(input())
M = int(input())
T = int(input())

t_h = int(T / 60)
t_m = T % 60

m = M + t_m
n = N + t_h + int(m / 60)

n = n % 24
m = m % 60

print(f"{n:02d}:{m:02d}")