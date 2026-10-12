"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        
        new_root=Node(node.val)
        visited={node:new_root}
        stack=[node]
        while stack:
            cur = stack.pop()
            new_cur=visited[cur]
            for neighbor in cur.neighbors:
                # if unvisited, append to stack and create new node, else simply add edge
                if neighbor not in visited:
                    new_neighbor=Node(neighbor.val)
                    visited[neighbor]=new_neighbor
                    stack.append(neighbor) 
                new_cur.neighbors.append(visited[neighbor])
        return new_root

            