# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None: return 0
        # return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        if root is None: return 0
        max_depth=0
        stack=[(root, 1)]
        while len(stack) > 0:
            node,depth = stack.pop()
            max_depth=max(depth,max_depth)
            if node.left is not None:
                stack.append((node.left, depth+1))
            if node.right is not None:
                stack.append((node.right, depth+1))
        return max_depth
        