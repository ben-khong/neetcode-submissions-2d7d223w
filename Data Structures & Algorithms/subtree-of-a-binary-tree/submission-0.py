# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, c1, c2):
        if not c1 and not c2:
            return True
        elif (not c1 or not c2) or c1.val != c2.val:
            return False
        else:
            return self.isSame(c1.left, c2.left) and self.isSame(c1.right, c2.right)