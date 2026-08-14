# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, cur, left, right):
        if not cur:
            return True 
        if cur.val <= left or right <= cur.val:
            return False 
        return self.isValid(cur.left, left, cur.val) and self.isValid(cur.right, cur.val, right)
    