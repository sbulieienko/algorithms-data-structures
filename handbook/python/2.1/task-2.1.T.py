N = int(input()) 
M = int(input())
K1 = int(input())
K2 = int(input())

x = N * (K2 - M) / (K2 - K1)

y = N * (M - K1) / (K2 - K1)

print(int(x), int(y))
