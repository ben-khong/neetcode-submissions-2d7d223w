# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(curr, largest):
            nonlocal res
            if not curr:
                return 0
            
            largest = max(largest, curr.val)

            if curr.val >= largest:
                res += 1

            dfs(curr.left, largest)
            dfs(curr.right, largest)

            

        dfs(root, root.val)
        return res
            
