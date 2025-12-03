# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            size = len(queue)
            lst = []
            level += 1
            for i in range(size):
                node = queue.popleft()
                lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(lst) if level % 2 != 0 else res.append(lst[::-1])
        return res
        
        