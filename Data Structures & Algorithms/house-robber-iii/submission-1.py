# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # with, without
        def dfs(root):
            if not root:
                return [0,0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            skip = max(left) + max(right)
            take = root.val + left[0] + right[0]

            return [skip, take]

        return max(dfs(root))
