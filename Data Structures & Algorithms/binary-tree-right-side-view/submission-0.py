# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result=[]
        cur_level=[root]
        while cur_level:
            next_level=[]
            for i, node in enumerate(cur_level):
                if i==len(cur_level)-1:
                    result.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            cur_level=next_level
        return result