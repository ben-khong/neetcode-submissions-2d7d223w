# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before, cur = dummy, head

        while True:
            if not self.enoughNodes(cur, k):
                break

            first = before.next

            prev = None
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur 
                cur = temp
            
            before.next.next = cur
            before.next = prev 

            before = first
        
        return dummy.next

    def enoughNodes(self, cur, k):
        for _ in range(k):
            if cur == None:
                return False
            cur = cur.next
        return True 

            
