"""
Создайте два связных списка: один круговой, а другой — без цикла.
Убедитесь, что в каждом из них есть метод detect_cycle для определения
того, имеется ли в списке цикл. Вызовите detect_cycle для обоих списков.
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
    
    def detect_cycle(self):
        """Использует алгоритм черепахи и зайца для определения цикла"""
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "\n".join(result)

# Создаем связный список БЕЗ цикла
list_without_cycle = LinkedList()
for i in range(1, 6):
    list_without_cycle.append(i)

# Создаем связный список С циклом
list_with_cycle = LinkedList()
for i in range(1, 6):
    list_with_cycle.append(i)

# Создаем цикл: последний узел указывает на третий узел
current = list_with_cycle.head
while current.next:
    current = current.next
current.next = list_with_cycle.head.next.next

# Печатаем списки
print("Список без цикла:")
print(list_without_cycle)

print("Список с циклом:")
print("Цикл создан, поэтому список не может быть выведен полностью.")

# Проверяем наличие циклов
print("Список без цикла содержит цикл:", list_without_cycle.detect_cycle())
print("Список с циклом содержит цикл:", list_with_cycle.detect_cycle())
