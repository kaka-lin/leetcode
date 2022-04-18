class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dict = {}
        for i in range(len(nums)):
            find_value = target - nums[i]
            if find_value in value_dict:
                return [value_dict[find_value], i]
            value_dict[nums[i]] = i
