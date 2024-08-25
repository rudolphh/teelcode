from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        orig_to_clone = {}

        def dfs(node):
            if node in orig_to_clone:
                return orig_to_clone[node]

            orig_to_clone[node] = Node(node.val)

            for neigh in node.neighbors:
                orig_to_clone[node].neighbors.append(dfs(neigh))

            return orig_to_clone[node]
                
        return dfs(node) if node else None
