class ListNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} 
        self.capacity = capacity

        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def add(self, node):
        prev, next = self.right.prev, self.right 
        prev.next = next.prev = node 
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
