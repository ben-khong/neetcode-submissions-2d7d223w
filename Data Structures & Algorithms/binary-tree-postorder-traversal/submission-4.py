# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[1, 3, 2, 5]
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res = [cur.val] + res
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()

        return res

            