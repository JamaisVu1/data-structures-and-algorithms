from data_structures.linked_list import LinkedList

def zip_lists(list1, list2):

    zipped_list = LinkedList()

    current1 = list1.head
    current2 = list2.head
    current = zipped_list.head

    while current1 or current2:
        if current1:
            zipped_list.append(current1.value)
            current1 = current1.next

        if current2:
            zipped_list.append(current2.value)
            current2 = current2.next

    return zipped_list