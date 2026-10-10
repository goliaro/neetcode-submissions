# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def isSameTree(self, root, subroot) -> bool:
    #     if (root is None) != (subroot is None):
    #         return False
    #     if root is None and subroot is None:
    #         return True
    #     if root.val != subroot.val:
    #         return False
    #     return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right) 
    
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if root is None: return False
    #     if self.isSameTree(root, subRoot): return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # in order traversal
        root_traversal=[]
        stack=[root]
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                root_traversal.append(None)
            else:
                root_traversal.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        subroot_traversal=[]
        stack=[subRoot]
        while len(stack) > 0:
            node=stack.pop()
            if node is None:
                subroot_traversal.append(node)
            else:
                subroot_traversal.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        # print(root_traversal)
        # print(subroot_traversal)
        if len(subroot_traversal) > len(root_traversal):
            return False
        for i in range(len(root_traversal)-len(subroot_traversal)+1):
            if root_traversal[i:i+len(subroot_traversal)] == subroot_traversal:
                return True
        return False
            
                

        