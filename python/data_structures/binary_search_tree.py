# GPT assisted
from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.add_recursive(self.root, value)

    def add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.add_recursive(node.right, value)

    def contains(self, value):
        return self.contains_recursive(self.root, value)

    def contains_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.contains_recursive(node.left, value)
        else:
            return self.contains_recursive(node.right, value)