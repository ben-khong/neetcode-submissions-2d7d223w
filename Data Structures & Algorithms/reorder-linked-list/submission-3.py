# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow
        slow = slow.next
        temp.next = None

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        cur1, cur2 = head, prev
        while cur2:
            temp1, temp2, = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1, cur2 = temp1, temp2

        cur2 = cur1
        




