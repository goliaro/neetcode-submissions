# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal
        stack=[]
        cur = root
        traversal=[]
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            traversal.append(cur.val)
            cur=cur.right
        for i, num in enumerate(traversal):
            if i==0:
                continue
            if num <= traversal[i-1]:
                return False
        return True