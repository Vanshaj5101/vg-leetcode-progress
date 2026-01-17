# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return (0, True)
            
            left_height, left_isbalanced = dfs(node.left)
            right_height, right_isbalanced = dfs(node.right)
            return (max(left_height, right_height) + 1, abs(left_height - right_height) <= 1 and left_isbalanced and right_isbalanced)
        
        return dfs(root)[1]
        

        
