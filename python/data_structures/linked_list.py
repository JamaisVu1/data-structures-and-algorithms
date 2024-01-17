# GPT assisted

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    """
    A LinkedList class 
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("k must be a non-negative integer")

        pointer1 = self.head
        pointer2 = self.head

        for _ in range(k):
            if pointer2 is None:
                raise TargetError("k is larger than the length of the list")
            pointer2 = pointer2.next

        
        if pointer2 is None:
            raise TargetError("k is larger than the length of the list")

        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1.value
        


class TargetError(Exception):
    pass
