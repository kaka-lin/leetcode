# Failed method
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:     
#         ans = []
#         max_len = 0
#         seen = {}
#         prev = 
    
#         for c in s:
#             if c not in seen:
#                 seen[c] = 1
#                 prev = c
#             else:    
#                 if len(seen) > max_len:
#                     max_len = len(seen)
#                     ans = seen
#                 seen = {}
#                 if c != prev:
#                     seen[prev] = 1
#                 seen[c] = 1
        
#         if len(seen) > max_len:
#             return len(seen)
#         return max_len

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int: 
#         length = len(s)
#         i = 0 # right_bound
#         hesh_map = {}
#         curr_window = max_window = 0

#         while i < length:
#             curr = s[i]
#             if curr in hesh_map:
#                 curr_window = min(i - hesh_map[curr] - 1, curr_window) + 1
#                 hesh_map[curr] = i
#             else:
#                 curr_window += 1
#                 hesh_map[curr] = i

#             if curr_window >= max_window:
#                 max_window = curr_window
            
#             i += 1
            
#         return max_window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        length = len(s)
        left = right = 0
        _map = [0] * 256 # char position
        max_window = 0

        for right in range(length):
            curr = ord(s[right])
            if _map[curr]:
                left = max(left, _map[curr])
            _map[curr] = right + 1
            max_window = max(max_window, right - left + 1)
         
        return max_window
    