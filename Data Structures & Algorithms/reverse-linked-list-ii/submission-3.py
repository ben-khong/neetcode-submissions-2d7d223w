# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before, cur = dummy, head

        i = 1
        while i < left:
            before = cur 
            cur = cur.next
            i += 1

        prev = None
        while i < right + 1:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1
        
        before.next.next = cur 
        before.next = prev

        return dummy.next



