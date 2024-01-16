# CHatGPT assisted
import pytest
from linked_list import LinkedList  

def test_empty_list_instantiation():
    ll = LinkedList()
    assert ll.head is None

def test_insert_into_list():
    ll = LinkedList()
    ll.insert(1)
    assert ll.head is not None
    assert ll.head.value == 1

def test_head_points_to_first_node():
    ll = LinkedList()
    ll.insert(1)
    assert ll.head.value == 1
    ll.insert(2)
    assert ll.head.value == 2 

def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.head.value == 3
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 1

def test_find_value_exists():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) is True

def test_find_value_not_exists():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(4) is False

def test_return_all_values():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.to_string() == "{ 3 } -> { 2 } -> { 1 } -> NULL"