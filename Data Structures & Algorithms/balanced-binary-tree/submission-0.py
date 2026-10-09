# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        balanced=True

        def dfs(node):
            nonlocal balanced
            d_l, d_r = 0, 0
            if node.left is not None:
                d_l=1+dfs(node.left)
            if node.right is not None:
                d_r = 1+dfs(node.right)
            if abs(d_l-d_r) > 1:
                balanced=False
            return max(d_l, d_r)
        dfs(root)
        return balanced