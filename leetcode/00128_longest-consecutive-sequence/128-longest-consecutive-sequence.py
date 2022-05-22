# HashSet and Intelligent Sequence Building
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        # O(n)
        num_set = set(nums)
        
        for num in nums:
            # O(1)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                longest_length = max(longest_length, current_length)
        
        return longest_length
        