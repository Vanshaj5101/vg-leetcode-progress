# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append(root)
        total = 0

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft() 
                if node.left and not node.left.left and not node.left.right:
                    total += node.left.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return total