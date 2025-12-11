"""
Реализуйте очередь с помощью двух стеков, чтобы временная сложность постановки в очередь была равна О(1).
"""
class Stack:
    """Простой класс стека"""
    def __init__(self):
        self.items = []
    
    def push(self, value):
        """Добавляет элемент в стек"""
        self.items.append(value)
    
    def pop(self):
        """Удаляет и возвращает верхний элемент"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Возвращает верхний элемент без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self.items) == 0


class QueueFromStacks:
    """Очередь, реализованная на двух стеках"""
    def __init__(self):
        self.input_stack = Stack()    # Стек для добавления элементов
        self.output_stack = Stack()   # Стек для удаления элементов
    
    def enqueue(self, value):
        """Добавляет элемент в очередь за O(1)"""
        self.input_stack.push(value)
    
    def dequeue(self):
        """Удаляет и возвращает первый элемент за O(n) амортизированно O(1)"""
        if self.output_stack.is_empty():
            # Переливаем все элементы из input_stack в output_stack
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        
        return self.output_stack.pop()
    
    def peek(self):
        """Возвращает первый элемент без удаления"""
        if self.output_stack.is_empty():
            while not self.input_stack.is_empty():
                self.output_stack.push(self.input_stack.pop())
        
        return self.output_stack.peek()
    
    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return self.input_stack.is_empty() and self.output_stack.is_empty()


# Примеры использования
queue = QueueFromStacks()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(f"Dequeue: {queue.dequeue()}")  # 1
print(f"Dequeue: {queue.dequeue()}")  # 2

queue.enqueue(5)

print(f"Dequeue: {queue.dequeue()}")  # 3
print(f"Dequeue: {queue.dequeue()}")  # 4
print(f"Dequeue: {queue.dequeue()}")  # 5
print(f"Is empty: {queue.is_empty()}")  # True