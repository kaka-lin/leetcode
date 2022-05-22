class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        ans = []
        
        for num in nums1:
            # if num not in seen:
            #     seen[num] = 1
            # else:
            #     seen[num] += 1
            seen[num] = seen.get(num, 0) + 1
            
        for num in nums2:
            if num in seen and seen[num] > 0:
                ans.append(num)
                seen[num] -= 1
        
        return ans
