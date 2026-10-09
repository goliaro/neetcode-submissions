# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self, root):
        if root is None: return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        # for any given node, max diameter either uses current node or doesn't
        # if it does, then diameter is max_depth(left) + max_depth(right)
        # if it does not, then the diameter is simply the max diameter of the children
        max_diameter_including_node = self.max_depth(root.left) + self.max_depth(root.right)
        max_diameter_not_including_node = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(max_diameter_including_node, max_diameter_not_including_node)
        