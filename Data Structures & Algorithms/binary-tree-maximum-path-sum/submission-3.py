# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Post order dfs traversal with global res variable 
Create a dfs helper func that takes in root
if not root return 0
create two variables that you can use for traversal and to get the max of left and right subtrees
set them to be the max of themselves and 0 to not deal with negatives 
return left plus right 

"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res = max(res, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)
        dfs(root)
        return res