# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts_map = {}
        
#         for num in nums:
#             if num not in counts_map:
#                 counts_map[num] = 1
#             else:
#                 counts_map[num] += 1
        
#         sorted_map = dict(sorted(counts_map.items(), 
#                                  reverse=True, 
#                                  key=lambda item: item[1]))
        
#         return [key for key,value in sorted_map.items()][:k]


# Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        number_count = {}

        # Create empty buckets
        for i in range(len(nums) + 1):
            buckets.append([])
            
        # Put element into different buckets based on the frequence
        ## 1. Count number, frequence
        for num in nums:
            if num not in number_count:
                number_count[num] = 1
            else:
                number_count[num] += 1

        ## 2. Put element            
        for num, freq in number_count.items():
            buckets[freq].append(num)
            
        # Sort the elements of each bucket
        for i in range(len(buckets)):
            buckets[i] = sorted(buckets[i])
        
        flat_list = []
        # traverse from right to left so number with higher frequency come first
        # 是因為我們是按照 counts 來排的，所以越右邊的，出現頻率越高
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    flat_list.append(num)
        
        return flat_list[:k]
        