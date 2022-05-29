# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
       
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])

#         return root


# DFS
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums))
    
    def dfs(self, nums, left, right):
        if left >= right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, left, mid)
        root.right = self.dfs(nums, mid+1, right)
        
        return root