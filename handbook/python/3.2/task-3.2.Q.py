"""
Теория шести рукопожатий гласит, что любые два человека на планете могут быть связаны друг с другом через максимум шесть знакомых.
Но мы не будем идти так далеко — давайте ограничимся двумя уровнями знакомства.

Напишите программу, которая по списку пар друзей для каждого человека определяет список его друзей второго уровня — то есть друзей его друзей, исключая его самого и его непосредственных друзей.

Формат ввода
В каждой строке записывается два имени.
Окончанием ввода служит пустая строка.

Формат вывода
Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.

Пример
Ввод:
Николай Фёдор
Николай Женя
Фёдор Женя
Фёдор Илья
Илья Фёдор

Вывод:
Женя: Илья
Илья: Женя, Николай
Николай: Илья
Фёдор: 
"""

level_1_friends = dict()
while True:
    line = input()
    if line == "":
        break
    name_1, name_2 = line.split()
    if name_1 not in level_1_friends:
        level_1_friends[name_1] = set()
    if name_2 not in level_1_friends:
        level_1_friends[name_2] = set()
    level_1_friends[name_1].add(name_2)
    level_1_friends[name_2].add(name_1)

level_2_friends = dict()
for name, friends in level_1_friends.items():
    level_2_friends[name] = set()
    for friend in friends:
        level_2_friends[name].update(level_1_friends[friend])
    level_2_friends[name].discard(name)
    level_2_friends[name].difference_update(friends)

for name in sorted(level_2_friends.keys()):
    print(name + ": " + ", ".join(sorted(level_2_friends[name])))
