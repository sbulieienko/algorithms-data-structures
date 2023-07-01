n = int(input())

ans = -1
hash_prev = 0

for i in range(n):
    b = int(input())

    h = b % 256
    r = (b // 256) % 256
    m = b // (256 ** 2)

    hash_check = ((m + r + hash_prev) * 37) % 256

    if hash_check != h or h >= 100:
        if ans == -1:
            ans = i

    hash_prev = h

print(ans)
    