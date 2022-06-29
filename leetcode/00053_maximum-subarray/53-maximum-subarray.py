# Divide and Conqure: O(nlogn)
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
        
#         mid = len(nums) // 2
        
#         # If the maximum subarray appears in left.
#         left_sum = self.maxSubArray(nums[:mid])
#         # If the maximum subarray appears in right.
#         right_sum = self.maxSubArray(nums[mid:])
#         # If the maximum subarray crosses the middle.
#         middle_sum = self.max_cross_subarray(nums[:mid], nums[mid:])
        
#         if left_sum >= right_sum and left_sum >= middle_sum:
#             return left_sum
#         elif right_sum >= left_sum and right_sum >= middle_sum:
#             return right_sum
#         else:
#             return middle_sum
        
#     def max_cross_subarray(self, left_list, right_list):
#         left_sum = float("-inf")
#         temp_sum = 0
#         for idx in range(len(left_list)-1, -1, -1):
#             temp_sum += left_list[idx]
#             if temp_sum > left_sum:
#                 left_sum = temp_sum
        
#         right_sum = float("-inf")
#         temp_sum = 0
#         for idx in range(len(right_list)):
#             temp_sum += right_list[idx]
#             if temp_sum > right_sum:
#                 right_sum = temp_sum
        
#         return left_sum + right_sum
                

# DP: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:    
        if nums is None:
            return 0
        
        length = len(nums)
        table = [0] * length
        table[0] = nums[0]
        _max = table[0]
        
        for i in range(1, length):
            if table[i-1] < 0:
                table[i] = nums[i]
            else:
                table[i] = table[i-1] + nums[i]
            
            if table[i] > _max:
                _max = table[i]

        return _max
