class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # rea, 0
        curr = 0 # white
        right = len(nums) - 1 # blue

        while (curr <= right):
            if nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            elif nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1
            else: # == 1
                curr += 1
