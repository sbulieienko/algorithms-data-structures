str1 = input()
str2 = input()

set1 = set(str1) & set(str2)

print(''.join(list(set1)))

