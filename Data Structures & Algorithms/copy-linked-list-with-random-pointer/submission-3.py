"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

Use a map to map nodes to their copies (map None to None)
First pass to create the copies and map them to their corresponding nodes
Second pass to link the pointers of the copies to other copies
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}
        cur = head

        # in the first pas we never set map None to None
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head 

        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]  
            copy.random = oldToCopy[cur.random] 
            cur = cur.next
        
        return oldToCopy[head] 

