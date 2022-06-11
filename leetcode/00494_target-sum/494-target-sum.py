# DFS
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.cache = {}
        return self.findTarget(nums, 0, S)  # (nums, idx, sum)
    
    def findTarget(self, nums, i, sum_):
        if (i, sum_) not in self.cache:
            if i == len(nums):
                # 因為一開始是傳 target 進來
                # 所以目標就是減至 0
                if sum_ == 0:
                    counts = 1
                else:
                    counts = 0
            else:
                counts = self.findTarget(nums, i+1, sum_+nums[i]) + \
                         self.findTarget(nums, i+1, sum_-nums[i])
            self.cache[(i, sum_)] = counts
        return self.cache[(i, sum_)]
    