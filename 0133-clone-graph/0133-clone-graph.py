"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        hshmap = {}
        def dfs(root):
            if root not in hshmap:
                new_node = Node(root.val)
                hshmap[root] = new_node
                for n in root.neighbors:
                    new_node.neighbors.append(dfs(n))
                return new_node
            else:
                return hshmap[root]

        dfs(node)
        return hshmap[node]
