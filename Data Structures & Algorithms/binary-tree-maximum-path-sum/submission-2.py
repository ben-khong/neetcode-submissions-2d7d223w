# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
postorder dfs traversal -> LRR

create a global result variable

create a dfs func that takes in a node and returns int
base case: if not node return 0
create left max and right max variables that recursively run the dfs in that direction
set them equal to the max of the left nodes value and 0 (because there are negative numbers)

update the res to be curr node value plus left and right max if it is larger (calculating the max if theres a split)

return curr node value plus max of leftmax or right max (calculating the total if there is no split)
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            nonlocal res 
            res = max(res, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return res