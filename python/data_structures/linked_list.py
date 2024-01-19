# GPT assisted

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current = self.head
        values = []
        while current:
            values.append(f"{{ {current.value} }}")
            current = current.next
        values.append("NULL")
        return " -> ".join(values)
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, value):
        new_node = Node(value)
        if not self.head:
            return
        if self.head.value == target:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.value != target:
            current = current.next
        if current.next:
            new_node.next = current.next
            current.next = new_node

    def insert_after(self, target, value):
        new_node = Node(value)
        current = self.head
        while current and current.value != target:
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node
            
