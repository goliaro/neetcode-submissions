# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None:
        #     return root
        # l=self.invertTree(root.right)
        # r=self.invertTree(root.left)
        # root.left=l
        # root.right=r
        # return root
        if root is None: return None
        q=deque([root])
        while len(q) > 0:
            cur = q.popleft()
            if cur is not None:
                temp=cur.left
                cur.left=cur.right
                cur.right=temp
                q.append(cur.left)
                q.append(cur.right)
        return root