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
