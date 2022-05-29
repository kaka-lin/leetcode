class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = self.merge_sort(nums)
        return ans
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        if left:
            result += left
        if right:
            result += right
            
        return result
        