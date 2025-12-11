"""
Инвертируйте двоичное дерево с помощью обхода в ширину (BFS).
"""

class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def invert_tree(self):
        """Инвертирует двоичное дерево с помощью обхода в ширину (BFS)"""
        if self is None:
            return None
        
        # Используем очередь для обхода в ширину
        queue = [self]
        
        # Обрабатываем узлы уровень за уровнем
        while queue:
            node = queue.pop(0)
            
            if node is not None:
                # Меняем местами левое и правое поддеревья
                node.left_child, node.right_child = node.right_child, node.left_child
                
                # Добавляем дочерние узлы в очередь
                if node.left_child is not None:
                    queue.append(node.left_child)
                if node.right_child is not None:
                    queue.append(node.right_child)
        
        return self

    def print_tree(self, level=0, prefix="Root: "):
        """Выводит структуру дерева"""
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.key))
            if self.left_child is not None or self.right_child is not None:
                if self.left_child:
                    self.left_child.print_tree(level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if self.right_child:
                    self.right_child.print_tree(level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)
print("Исходное дерево:")
tree.print_tree()

print("\n" + "="*50)
print("Инвертированное дерево:")
tree.invert_tree()
tree.print_tree()