N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))

pow = int(input())

for num in nums:
    print(num**pow)
