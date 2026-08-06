class Node:
    def __init__(self, key, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None 
# Create Node Class with next and prev pointer for a doubly linked list
class LRUCache:
    # Create a map (key->NodeObj) and two node objects that point to the least and most recently used
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    # Create a remove method that updates the pointers surrounding a node  
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Create a insert method that updates the pointers surrounding a node 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    
    # Check if key in cache, call remove and insert methods, then return the val. If not return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    # Check if the key is in cache, if so, call remove method. If not, create a Node obj and use insert method. Check capacity, if more than capacity, get the lru from the left pointer and call remove method and delete the key
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
