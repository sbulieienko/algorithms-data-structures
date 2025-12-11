"""
Добавьте в код вашего двоичного дерева метод под названием has_leaf_nodes.
Метод должен вернуть True, если у дерева есть узлы без листов, и False, если их нет
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

    def has_leaf_nodes(self):
        if self is None:
            return False
        if self.left_child is None and self.right_child is None:
            return True
        left_has_leaf = self.left_child.has_leaf_nodes() if self.left_child else False
        right_has_leaf = self.right_child.has_leaf_nodes() if self.right_child else False
        return left_has_leaf or right_has_leaf


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)

print(tree.has_leaf_nodes())  # True