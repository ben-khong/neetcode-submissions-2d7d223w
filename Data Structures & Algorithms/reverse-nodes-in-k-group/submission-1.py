# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        while True:
            kth = self.getKth(before, k)
            if not kth:
                break
            after = kth.next

            prev, cur = kth.next, before.next
            while cur != after:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = before.next
            before.next = kth
            before = temp
        
        return dummy.next

    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

        
        
