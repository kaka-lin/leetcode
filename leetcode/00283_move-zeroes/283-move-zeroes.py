class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[change_index] = nums[change_index], nums[i]
                change_index += 1
                