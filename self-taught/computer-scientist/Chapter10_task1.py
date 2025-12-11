"""
Создайте связный список, содержащий числа от 1 до 100. Затем выведите каждый узел списка.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "\n".join(result)

# Создаем связный список с числами от 1 до 100
linked_list = LinkedList()
for i in range(1, 101):
    linked_list.append(i)

# Выводим каждый узел списка
print(linked_list)