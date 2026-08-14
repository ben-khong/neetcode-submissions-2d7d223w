# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
edgecase where no root -> return 0
dfs traversal, postorder
keep a global variable of good node initially set to 1
create dfs helper function returns int
    if 
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.goodNodes = 0
        def dfs(cur, cur_max):
            if not cur:
                return 
            if cur.val >= cur_max:
                self.goodNodes += 1
            dfs(cur.left, max(cur.val, cur_max))
            dfs(cur.right, max(cur.val, cur_max))

        dfs(root, root.val)
        return self.goodNodes

            