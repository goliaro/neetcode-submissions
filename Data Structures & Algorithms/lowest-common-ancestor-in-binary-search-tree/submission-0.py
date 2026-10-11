# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l,h=min(p.val,q.val), max(p.val,q.val)

        cur = root
        while cur.val > h or cur.val < l:
            if cur.val > h:
                cur = cur.left
            elif cur.val < l:
                cur = cur.right
        return cur
