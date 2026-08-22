# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val and cur.left:
                cur = cur.left
            elif cur.val < val and cur.right:
                cur = cur.right
            elif val < cur.val:
                cur.left = TreeNode(val)
                break
            elif cur.val < val:
                cur.right = TreeNode(val)
                break
            

        return root
            

