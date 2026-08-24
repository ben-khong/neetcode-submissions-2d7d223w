# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res 

        # def dfs(root):
        #     nonlocal res
        #     if not root:
        #         return 
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)
        # return res


