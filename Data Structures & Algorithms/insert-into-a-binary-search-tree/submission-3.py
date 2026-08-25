# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(curr, val):
            if not curr:
                return TreeNode(val)
            elif val < curr.val: 
                curr.left = dfs(curr.left, val)
            elif val > curr.val:
                curr.right = dfs(curr.right, val)
            return curr
        
        return dfs(root, val) 


