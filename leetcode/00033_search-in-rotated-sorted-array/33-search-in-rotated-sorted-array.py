class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # checking first half array is sorted or not
            if nums[mid] >= nums[left]:
                # checking target is exist in first half or not
                # left -> targt -> mid
                if (target >= nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # checking for target exist in second half or not
                # mid -> target -> right
                if (target <= nums[right] and target > nums[mid]):
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
