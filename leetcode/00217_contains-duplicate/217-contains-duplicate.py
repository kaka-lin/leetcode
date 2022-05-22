# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = {}
        
#         for num in nums:
#             if num not in seen:
#                 seen[num] = 1
#             else:
#                 seen[num] += 1
#                 return True
        
#         return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    