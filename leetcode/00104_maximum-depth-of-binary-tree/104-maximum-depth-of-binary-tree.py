# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Top-down
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         self.ans = 0   
#         self.preorder(root, 1)
#         return self.ans
    
#     # preoder: top-down   
#     def preorder(self, root, depth):
#         if not root:
#             return 0
        
#         if self.ans < depth:
#             self.ans = depth
        
#         self.preorder(root.left, depth + 1)
#         self.preorder(root.right, depth + 1)

# Bottom-up
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1
        