# GPT assisted
from data_structures.queue import Queue


def multi_bracket_validation(string):
    queue = Queue()
    temp_storage = []
    bracket_mapping = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char in bracket_mapping or char in bracket_mapping.values():
            queue.enqueue(char)

    while not queue.is_empty():
        char = queue.dequeue()

        if temp_storage and temp_storage[-1] == bracket_mapping.get(char, None):
            temp_storage.pop() 
        else:
            temp_storage.append(char)

    return len(temp_storage) == 0

