str1 = input()

str1_list = str1.split()

sum1 = 0

for item in str1_list:
    sum1 += int(item)

print(sum1)