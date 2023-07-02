def greatest_common_divisor(a, b):
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
    return big


count1 = int(input())
gcd = None

for i in range(count1):
    n = int(input())
    if gcd is None:
        gcd = n
    else:
        gcd = greatest_common_divisor(n, gcd)

print(gcd)
