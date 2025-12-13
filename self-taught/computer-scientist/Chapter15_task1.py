"""
Напишите функцию, которая принимает двоичное дерево в качестве параметра и возвращает True, если это минимальная куча, и False, если нет.
"""

def is_min_heap(tree):
    # Проверяем, что каждый родительский узел меньше или равен своим дочерним узлам
    n = len(tree) 
    # Проходим по всем родительским узлам
    for i in range((n - 2) // 2 + 1):
    # Формулы для индексов потомков в массивном представлении двоичного дерева:
    # - Для узла с индексом i (корень имеет индекс 0):
    #     левый потомок:  2 * i + 1
    #     правый потомок: 2 * i + 2
    # Эти формулы возникают из заполнения уровней слева направо в массиве
    # (представление complete/heap-дерева). Если left = 2*i + 1 < n,
    # то у узла i есть хотя бы один потомок. Следовательно, максимальный
    # индекс i, для которого может существовать левый потомок, удовлетворяет
    # 2*i + 1 <= n - 1  =>  i <= (n - 2) / 2. Поэтому в целочисленном
    # переборе используем (n - 2) // 2 + 1, чтобы пройти все такие i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and tree[i] > tree[left]:
            return False
        if right < n and tree[i] > tree[right]:
            return False
    return True


def print_heap_tree(tree):
    """Визуализирует массивное представление двоичного дерева по уровням.

    Выводит каждый уровень дерева на отдельной строке. Подходит для маленьких деревьев.
    """
    if not tree:
        print("<empty>")
        return

    n = len(tree)
    level = 0
    index = 0
    # Для каждого уровня выводим элементы с индексов 2^level -1 до 2^(level+1)-2
    while index < n:
        level_count = 2 ** level
        level_items = tree[index: index + level_count]
        # Форматируем строку: разделяем элементы пробелом
        print(" ".join(str(x) for x in level_items))
        index += level_count
        level += 1


input_tree = [1, 3, 5, 7, 9, 11]
print("Tree:")
print_heap_tree(input_tree)
print("is_min_heap:", is_min_heap(input_tree))  # Ожидаемый вывод: True

input_tree = [10, 40, 20, 30, 25, 15]
print("\nTree:")
print_heap_tree(input_tree)
print("is_min_heap:", is_min_heap(input_tree))  # Ожидаемый вывод: False

input_tree = [2, 4, 6, 8, 10, 12]
print("\nTree:")
print_heap_tree(input_tree)
print("is_min_heap:", is_min_heap(input_tree))  # Ожидаемый вывод: True




