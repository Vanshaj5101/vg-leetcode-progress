"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            if not node.children:
                return 1
            depth = []
            for n in node.children:
                depth.append(dfs(n))
            return max(depth) + 1
        
        return dfs(root)