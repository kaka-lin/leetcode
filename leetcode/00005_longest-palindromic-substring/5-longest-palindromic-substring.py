# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         length = len(s)
#         max_window = 1
#         start = end = 0

#         for i in range(length):
#             odd = self.palindromeAt(s, i, i) # 單數框
#             even = self.palindromeAt(s, i, i+1) # 偶數框

#             _len = odd if odd >= even else even
#             if (_len > max_window):
#                 max_window = _len
#                 start = i - (_len - 1) // 2
#                 end = i + _len // 2
        
#         return s[start:end+1]
    
#     # starting at l,r expand outwards to find the biggest palindrome
#     # get the longest palindrome, l, r are the middle indexes   
#     # from inner to outer
#     def palindromeAt(self, s, l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
        
#         # 因為 left 與 right 會停在 s[left] != s[right]
#         #   => window 大小會多 "2"
#         # 但因為 index 是從 0 開始
#         #   => 所以 right - left - 1 即為 window 大小
#         return r - l - 1


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.palindromeAt(s, i, i) # 單數框
            even = self.palindromeAt(s, i, i+1) # 偶數框

            res = max(res, odd, even, key=len)
        
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def palindromeAt(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1:r]
        