# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
        
#         ans = []
#         self.helper(root, ans)
#         return ans
    
#     def helper(self, root, ans):
#         if root.left:
#             self.helper(root.left, ans)
        
#         ans.append(root.val)
        
#         if root.right:
#             self.helper(root.right, ans)
  
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans
    