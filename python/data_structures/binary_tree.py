# GPT assisted

class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        def walk(node):
            if node is None:
                return []
            return [node.value] + walk(node.left) + walk(node.right)
        return walk(self.root)

    def in_order(self):
        def walk(node):
            if node is None:
                return []
            return walk(node.left) + [node.value] + walk(node.right)
        return walk(self.root)

    def post_order(self):
        def walk(node):
            if node is None:
                return []
            return walk(node.left) + walk(node.right) + [node.value]
        return walk(self.root)
        
        

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

