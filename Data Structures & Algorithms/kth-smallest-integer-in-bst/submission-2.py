# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

        8
    6       14
  1   7   13   16 
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()

            if k == 1:
                return cur.val
            k -= 1

            cur = cur.right
        

        
            
        


        