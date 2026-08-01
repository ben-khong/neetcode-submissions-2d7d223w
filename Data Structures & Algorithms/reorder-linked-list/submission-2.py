# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Split the list into two 
reverse the second list
reorder the pointers  
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle and partition it
        slow, fast = head, head.next

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # [1, 2, 3, 4, 5] => [1, 2] [3, 4, 5]
        # [1, 2, 3, 4] => [1, 2] [3, 4]

        temp = slow
        slow = slow.next
        temp.next = None

        # reverse the right list 
        prev2 = None
        while slow:
            temp = slow.next
            slow.next = prev2
            prev2 = slow
            slow = temp

        # reorder pointers
        cur1, cur2 = head, prev2
        while cur1.next:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1, cur2 = temp1, temp2
        
        cur1.next = cur2


            
           

            


        
            

        
        