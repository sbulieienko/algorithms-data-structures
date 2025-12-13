"""
Главный повар детского сада хочет быстрее определять, какие блюда можно приготовить на обед.
У него есть список доступных продуктов и список рецептов.

Напишите программу, которая по списку имеющихся продуктов и рецептам определяет, какие блюда можно приготовить.

Формат ввода
Число продуктов (N), которые имеются в наличии.
N строк с названиями продуктов.
Число рецептов (M), о которых имеется информация.
M блоков строк для каждого из рецептов.
В первой строке каждого блока записано название блюда.
Во второй — число ингредиентов.
Затем перечисляются сами ингредиенты, требуемые для приготовления блюда.

Формат вывода
Список блюд, которые можно приготовить в алфавитном порядке.
Если ни одно из блюд нельзя приготовить, следует вывести «Готовить нечего».

Пример

Ввод:
4
Яблоки
Хлеб
Варенье
Картошка
3
Тосты
2
Хлеб
Варенье
Яблочный Сок
1
Яблоки
Яичница
1
Яйца

Вывод:
Тосты
Яблочный Сок
"""

N = int(input())
products = set()
for _ in range(N):
    products.add(input())

M = int(input())
recipes = {}
for _ in range(M):
    recipy_name = input()
    recipy_ingredients = set()
    for _ in range(int(input())):
        recipy_ingredients.add(input())
    recipes[recipy_name] = recipy_ingredients

possible_recipes = set()
for recipy_name, recipy_ingredients in recipes.items():
    if recipy_ingredients.issubset(products):
        possible_recipes.add(recipy_name)

if len(possible_recipes) == 0:
    print("Готовить нечего")
else:
    for recipy_name in sorted(possible_recipes):
        print(recipy_name)
