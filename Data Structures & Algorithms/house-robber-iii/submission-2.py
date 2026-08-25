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
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            skip = max(leftPair) + max(rightPair)
            take = root.val + leftPair[0] + rightPair[0]

            return [skip, take]

        return max(dfs(root))
