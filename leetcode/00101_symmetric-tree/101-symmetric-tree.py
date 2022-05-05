# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We go down from the root and check if they have the same value
# After the first lvl we sould compare:
#   (left.left to right.right) and (left.right to right.left).
# Untill we get to the end of the tree.
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return self.helper(root, root)
    
#     def helper(self, l, r):
#         if not l and not r:
#             return True
        
#         if l and r and l.val == r.val:
#             return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        
#         return False

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        stack = [root, root]
        
        while stack:
            left = stack.pop(0)
            right = stack.pop(0)
            
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            
            stack.extend([left.left, right.right, left.right, right.left])
            
        return True
