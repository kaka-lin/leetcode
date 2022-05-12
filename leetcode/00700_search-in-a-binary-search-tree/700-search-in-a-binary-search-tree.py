# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         while root:
#             if val == root.val:
#                 return root
#             elif val < root.val:
#                 root = root.left
#             else:
#                 root = root.right
#      
#         return None

# recursive
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
    
        if val == root.val:
            return root
        
        ans = None
        if val < root.val:
            ans = self.searchBST(root.left, val)
        else:
            ans = self.searchBST(root.right, val)
        
        return ans
        