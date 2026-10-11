# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # definitely a bfs. The issue is knowing when each layer ends. Guess we can keep track of current level?
        if root is None: return []
        result=[]
        current_level=[root]
        while current_level:
            res=[0]*len(current_level)
            next_level=[]
            for i,node in enumerate(current_level):
                res[i]=node.val
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            result.append(res)
            current_level=next_level
        return result