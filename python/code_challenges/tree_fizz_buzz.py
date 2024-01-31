from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(kary_tree):
    def fizz_buzz(value):
        result = ''
        if value % 3 == 0:
            result += 'Fizz'
        if value % 5 == 0:
            result += 'Buzz'
        if result == '':
            result = str(value)
        return result

    def clone_with_fizz_buzz(node):
        if node is None:
            return None

        new_node = Node(fizz_buzz(node.value))
        for child in node.children:
            new_child = clone_with_fizz_buzz(child)
            if new_child:
                new_node.add_child(new_child)

        return new_node

    new_root = clone_with_fizz_buzz(kary_tree.root)
    return KaryTree(new_root)