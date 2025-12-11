"""
Инвертируйте двоичное дерево с помощью обхода в глубину (DFS).
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
        """Инвертирует двоичное дерево с помощью обхода в глубину (DFS)"""
        if self is None:
            return None
        
        # Меняем местами левое и правое поддеревья текущего узла
        self.left_child, self.right_child = self.right_child, self.left_child
        
        # Рекурсивно инвертируем левое поддерево
        if self.left_child is not None:
            self.left_child.invert_tree()
        
        # Рекурсивно инвертируем правое поддерево
        if self.right_child is not None:
            self.right_child.invert_tree()
        
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