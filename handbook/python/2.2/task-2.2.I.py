name1 = input()
name2 = input()
name3 = input()

min_name = min(name1, name2, name3)

if min_name == name1:
    print(name1)
elif min_name == name2:
    print(name2)
else:
    print(name3)
