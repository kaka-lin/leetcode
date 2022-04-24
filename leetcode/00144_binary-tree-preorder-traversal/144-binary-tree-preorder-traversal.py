# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: recursive
# Time: O(N)
# Space: worst-O(N), average-O(logn)
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if root is None:
#             return []

#         array = []
#         self.preorderHelper(root, array)
#         return array

#     def preorderHelper(self, root: TreeNode, array: List[int]):
#         array.append(root.val)

#         if root.left:
#             self.preorderHelper(root.left, array)

#         if root.right:
#             self.preorderHelper(root.right, array)

            
# Solution 2: Iterating
# Time: O(N)
# Spave: O(N)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        
        while root:
            ans.append(root.val)
                        
            if root.right:
                stack.append(root.right)
            
            if root.left:
                root = root.left
            elif stack:
                root = stack.pop()
            else:
                break
        
        return ans
    