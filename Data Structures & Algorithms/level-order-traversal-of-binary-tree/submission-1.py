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
        nodes_this_layer=1
        queue=deque([root])
        while len(queue) > 0:
            res=[None]*nodes_this_layer
            nodes_next_layer=0
            for i in range(nodes_this_layer):
                node = queue.popleft()
                res[i]=node.val
                if node.left is not None:
                    queue.append(node.left)
                    nodes_next_layer+=1
                if node.right is not None:
                    queue.append(node.right)
                    nodes_next_layer+=1
            result.append(res)
            nodes_this_layer=nodes_next_layer
        return result