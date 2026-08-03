# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
first split the list into two 
reverse the second list
rearrange the pointers by traversing through the two lists
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None 

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        cur1, cur2 = head, prev
        while cur2:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1 
            cur1, cur2 = temp1, temp2

