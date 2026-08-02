# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        after = dummy

        while n > 0:
            after = after.next
            n -= 1
        
        before = dummy

        while after and after.next:
            before = before.next
            after = after.next
            
        before.next = before.next.next

        return dummy.next
        
        