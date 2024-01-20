class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    pass

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        pop_value = self.top.value
        self.top = self.top.next
        return pop_value

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return self.top is None
