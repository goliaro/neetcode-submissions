# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue=deque([(p,q)])
        while len(queue) > 0:
            a,b = queue.popleft()
            if (a is None and b is not None) or (a is not None and b is None) or (a is not None and b is not None and a.val != b.val):
                return False
            if a is not None:
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
        return True