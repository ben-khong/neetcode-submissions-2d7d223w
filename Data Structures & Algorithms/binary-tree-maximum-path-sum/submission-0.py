# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            left = max(left, 0)
            right = max(right, 0)

            res[0] = max(res[0], curr.val + left + right)

            return curr.val + max(left, right)
        
        dfs(root)

        return res[0]


