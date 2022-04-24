# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        self.maxDepth = 0
        depth = 1
        self.DFS(root, depth)
        return self.maxDepth
    
    def DFS(self, root, depth):
        if root.left:
            self.DFS(root.left, depth+1)
        
        if root.right:
            self.DFS(root.right, depth+1)
        
        if depth > self.maxDepth:
            self.maxDepth = depth
        