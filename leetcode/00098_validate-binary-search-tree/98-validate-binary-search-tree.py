# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: Recursion
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         return self.helper(root, float("-inf"), float("inf"))
        
#     def helper(self, root, min_val, max_val):
#         if not root:
#             return True
        
#         if root.val <= min_val or root.val >= max_val:
#             return False
        
#         return self.helper(root.left, min_val, root.val) and \
#                self.helper(root.right, root.val, max_val)


# Solution 2: Inorder traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float("-inf")
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
        
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        
        return True   
