"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = list()

        while queue:
            lst = list()
            for i in range(len(queue)):
                node = queue.popleft()
                lst.append(node.val)
                queue.extend(node.children)
            res.append(lst)

        return res