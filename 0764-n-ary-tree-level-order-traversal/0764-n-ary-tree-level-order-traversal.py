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
            size = len(queue)
            lst = list()
            for i in range(size):
                node = queue.popleft()
                lst.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(lst)
    

        return res