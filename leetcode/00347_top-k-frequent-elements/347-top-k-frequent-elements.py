class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_map = {}
        
        for num in nums:
            if num not in counts_map:
                counts_map[num] = 1
            else:
                counts_map[num] += 1
        
        sorted_map = dict(sorted(counts_map.items(), 
                                 reverse=True, 
                                 key=lambda item: item[1]))
        
        return [key for key,value in sorted_map.items()][:k]
        