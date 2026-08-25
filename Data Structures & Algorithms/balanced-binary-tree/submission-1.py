# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def maxDepth(curr):
            nonlocal res
            if not curr:
                return 0
                
            left = maxDepth(curr.left)
            right = maxDepth(curr.right)

            if abs(left - right) > 1:
                res = False
            
            return 1 + max(left, right)
        
        maxDepth(root)
        return res

        