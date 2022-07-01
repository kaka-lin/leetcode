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
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = sorted(nums)
#         return nums[-k]


# DC, Quick Selection with Lomuto Partition Scheme
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = self.partition(nums, 0, len(nums)-1)   

        # example: 
        #   321   4    65, k = 2, len(nums)=6
        #        pos,3
        # k < 右半邊的數量 (k < len(nums) - pos): 答案就在右半邊: 第 k 個大的
        # k > 右半邊的數量 (k > len(nums) - pos): 答案就在左半邊: 第 k - 右半邊數量
        if k > len(nums) - pos: 
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos)) 
        elif k < len(nums) - pos:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]
    
    # Lomuto partition scheme   
    def partition(self, nums, lo, hi):
        index = random.randint(0, len(nums) - 1)
        nums[index], nums[hi] = nums[hi], nums[index]
        
        # 選出 pivot
        pivot = nums[hi]
        
        # 遍歷陣列，將小於等於 pivot 的元素和 i 位置的元素交換
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        # 將 pivot 和與第 i 個元素交換: 就切成兩半邊
        nums[i], nums[hi] = nums[hi], nums[i]
        return i
