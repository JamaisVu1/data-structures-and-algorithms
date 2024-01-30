# GPT Assisted
from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    if not tree.root:
        return []

    queue = [tree.root]
    values = []

    while queue:
        current = queue.pop(0) 
        values.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values