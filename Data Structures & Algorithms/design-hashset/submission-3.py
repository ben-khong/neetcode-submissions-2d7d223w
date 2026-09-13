"""
Just to clarify, what do you mean by built-in hash table libraries?

From my understanding, a hashset is a data structure that stores unique values.
It also has no indicies and can't modify the values (but you can pop and append).

Are all the operation O(1)?

Create ListNode class that contains key and next variables 

In constructor, list of ListNodes that each represent an index (we'll have as many nodes as there are operations)  
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_set = [Node(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = self.hash(key)
        cur = self.hash_set[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.hash_set[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        cur = self.hash_set[index]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


    def hash(self, key: int) -> int:
        index = key % len(self.hash_set)
        return index
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)