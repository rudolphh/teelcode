from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        created = {}

        q = deque()
        q.append(node)

        created[node] = Node(node.val)

        while q:
            n = q.popleft()
        
            for neighbor in n.neighbors:
                if neighbor not in created:
                    created[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                created[n].neighbors.append(created[neighbor])


        return created[node]
