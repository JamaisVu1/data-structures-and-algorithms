# ChatGPT assisted
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
            
    
def test_add_node_to_end():
    ll = LinkedList()
    ll.append(1)
    assert ll.to_string() == "{ 1 } -> NULL"

def test_add_multiple_nodes_to_end():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_string() == "{ 1 } -> { 2 } -> { 3 } -> NULL"

def test_insert_node_before_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 1.5)
    assert ll.to_string() == "{ 1 } -> { 1.5 } -> { 2 } -> { 3 } -> NULL"

def test_insert_node_before_first():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert_before(1, 0)
    assert ll.to_string() == "{ 0 } -> { 1 } -> { 2 } -> NULL"

def test_insert_node_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 2.5)
    assert ll.to_string() == "{ 1 } -> { 2 } -> { 2.5 } -> { 3 } -> NULL"

def test_insert_node_after_last():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 4)
    assert ll.to_string() == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL"