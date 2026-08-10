# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy

        while cur and n > 0:
            cur = cur.next
            n -= 1
        
        cur2 = dummy
        while cur and cur.next:
            cur = cur.next
            cur2 = cur2.next

        cur2.next = cur2.next.next

        return dummy.next
            
