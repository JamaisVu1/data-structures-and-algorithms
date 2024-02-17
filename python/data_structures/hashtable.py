from data_structures.linked_list import LinkedList , Node

#ChatGPT assisted
class Hashtable:
   
    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size

    def _hash(self, key):
       
        return hash(key) % self._size

    def set(self, key, value):
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = LinkedList()
        bucket = self._buckets[index]

        current = bucket.head
        while current:
            if current.value[0] == key:
                current.value[1] = value 
                return
            current = current.next

        bucket.insert([key, value])

    def get(self, key):
        
        index = self._hash(key) 
        bucket = self._buckets[index]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.value[0] == key:  
                    return current.value[1]  
                current = current.next 
        return None

    def has(self, key):
        index = self._hash(key)  
        bucket = self._buckets[index]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.value[0] == key:  
                    return True
                current = current.next  
        return False

    def keys(self):
   
        keys_list = []
        for bucket in self._buckets:
            current = bucket.head if bucket else None
            while current:
                key = current.value[0]  
                if key not in keys_list:
                    keys_list.append(key)
                current = current.next  
        return keys_list
