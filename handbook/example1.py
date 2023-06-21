
#name = input("Введите имя пользователя: ")
name = "Пользователь"

# print("Добрый день, ", name, ".", sep="")
print(f"Добрый день, {name}.")

print("Сложно" + "подчинённый")

print("-" * 80)

n_1 = "1"
n_2 = "2"
print(n_1 + n_2)
n_1 = int(n_1)
n_2 = int(n_2)
print(n_1 + n_2)

print("-" * 80)

x = 3.89
x = int(x)
print(x)

print("-" * 80)

width = "3.7"
height = "2.5"
s = float(width) * float(height)
print(s)

print("-" * 80)

#int_number = int(input())
#float_number = float(input())

n = 25
x = 0.5

print(n + x)
print(n - x)
print(n * x)
print(n / x)
print(n ** x)

print("-" * 80)

last_digit = 1234 % 10

my_in = input()

for i in range(0,2):
    print(my_in)

print("-" * 80)

preis = int(input())
gewicht = int(input())
geld = int(input())

print(int( geld - preis * gewicht ))    