class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    pass

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty queue.")
        dequeue_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return dequeue_value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty queue.")
        return self.front.value

    def is_empty(self):
        return self.front is None