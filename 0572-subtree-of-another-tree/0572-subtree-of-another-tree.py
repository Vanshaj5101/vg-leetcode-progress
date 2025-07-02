# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def subtree(root, subRoot):
            if not root and not subRoot:
                return True
            if (root and not subRoot) or (not root and subRoot) or (root.val != subRoot.val):
                return False
            return subtree(root.left, subRoot.left) and subtree(root.right, subRoot.right)
            
        if root.val == subRoot.val:
            if subtree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
