# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
head=[1,2,3]
left=2
right=3
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = cur = dummy

        for _ in range(left):
            before = cur
            cur = cur.next
        
        prev = None
        for _ in range(left, right+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        before.next.next = cur
        before.next = prev
        
        return dummy.next


        
        

        

        

       