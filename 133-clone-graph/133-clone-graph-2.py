from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}

        def dfs_clone(n):

            if n in created:
                return created[n]
            
            clone = Node(n.val)
            created[n] = clone

            for neighbor in n.neighbors:
                clone.neighbors.append(dfs_clone(neighbor))

            return clone
        

        return dfs_clone(node) if node else None
