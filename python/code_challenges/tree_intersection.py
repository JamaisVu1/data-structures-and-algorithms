from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    if not tree1.root or not tree2.root:
        return set()

    hash_table = Hashtable()
    result_set = set()

    def visit_insert(node):
        hash_table.insert(node.value)

    def visit_check(node):
        if hash_table.contains(node.value):
            result_set.add(node.value)

    tree1.pre_order(tree1.root, visit_insert)
    tree2.pre_order(tree2.root, visit_check)

    return result_set
