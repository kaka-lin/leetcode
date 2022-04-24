# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
        
#         ans = []
#         self.helper(root, ans)
#         return ans
    
#     def helper(self, root, ans):
#         if root.left:
#             self.helper(root.left, ans)
        
#         if root.right:
#             self.helper(root.right, ans)
        
#         ans.append(root.val)


# Solution 2: Iterating
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre = None
        stack = []
        ans = []
     
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.right and pre != root.right:
                stack.append(root)
                root = root.right
                continue
            
            ans.append(root.val)
            pre = root
            root = None
        
        return ans