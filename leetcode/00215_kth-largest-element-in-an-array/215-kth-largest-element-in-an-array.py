# Merge Sort
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = self.merge_sort(nums)
#         return nums[-k]
    
#     def merge_sort(self, nums):
#         if len(nums) <= 1:
#             return nums
        
#         mid = len(nums) // 2
#         left = self.merge_sort(nums[:mid])
#         right = self.merge_sort(nums[mid:])
#         return self.merge(left, right)
        
#     def merge(self, left, right):
#         ans = []
#         while left and right:
#             if left[0] < right[0]:
#                 ans.append(left.pop(0))
#             else:
#                 ans.append(right.pop(0))
        
#         if left:
#             ans += left
#         if right:
#             ans += right
        
#         return ans
    
    
# Built-in sorted method
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]