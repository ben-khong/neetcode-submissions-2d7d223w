"""
Just to clarify, by built-in hash table libraries that means no .get(), .items(), etc?

We aren't allowed to use {}?

Create a list node class that contains key, val, next vars

In the constructor, we'd create a list of dummy list nodes, one for every index  

helper hash function 
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash_map = [ListNode(0,0) for _ in range(10**4)]

    def hash(self, key: int) -> int:
        index = key % len(self.hash_map)
        return index

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.hash_map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return 
            cur = cur.next
        cur.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.hash_map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.hash_map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)