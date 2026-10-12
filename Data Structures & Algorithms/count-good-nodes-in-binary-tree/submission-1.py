# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_so_far):
            good=1 if root.val>=max_so_far else 0
            max_so_far=max(root.val, max_so_far)
            good += dfs(root.left, max_so_far) if root.left is not None else 0
            good += dfs(root.right, max_so_far) if root.right is not None else 0
            return good
        return dfs(root,root.val)