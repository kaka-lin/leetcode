class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        """
        在固定第一個數v的狀況，那當其中一個數為x，
        另一個數只能是-v-x(因為加總要等於0)。
        故每次將對應的互補數加入到dict中，
        我們只要從頭到尾檢查，即可得到所有的正確組合。
        """
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]): # 因為一次看三個
            if i >= 1 and v == nums[i-1]: # sort後，不用處理一樣的數
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))

        return list(res)
    