"""
Создайте максимальный стек, который позволит проталкивать, выталкивать
и отслеживать самое большое число вашего стека за время О(1).
"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []  # Дополнительный стек для отслеживания максимумов
    
    def push(self, value):
        """Добавляет элемент в стек за O(1)"""
        self.stack.append(value)
        
        # Добавляем в max_stack максимум между текущим значением и предыдущим максимумом
        if not self.max_stack:
            self.max_stack.append(value)
        else:
            self.max_stack.append(max(value, self.max_stack[-1]))
    
    def pop(self):
        """Удаляет элемент из стека за O(1)"""
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()
    
    def get_max(self):
        """Возвращает максимальный элемент за O(1)"""
        if not self.max_stack:
            return None
        return self.max_stack[-1]
    
    def peek(self):
        """Возвращает верхний элемент без удаления"""
        if not self.stack:
            return None
        return self.stack[-1]
    
    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self.stack) == 0


# Примеры использования
max_stack = MaxStack()

max_stack.push(5)
print(f"Push 5, Max: {max_stack.get_max()}")  # Max: 5

max_stack.push(10)
print(f"Push 10, Max: {max_stack.get_max()}")  # Max: 10

max_stack.push(3)
print(f"Push 3, Max: {max_stack.get_max()}")  # Max: 10

max_stack.push(15)
print(f"Push 15, Max: {max_stack.get_max()}")  # Max: 15

print(f"Pop: {max_stack.pop()}, Max: {max_stack.get_max()}")  # Pop: 15, Max: 10

max_stack.push(8)
print(f"Push 8, Max: {max_stack.get_max()}")  # Max: 10

print(f"Pop: {max_stack.pop()}, Max: {max_stack.get_max()}")  # Pop: 8, Max: 10
