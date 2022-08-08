# Dynamic Programming
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         left = right = 0
#         max_length = 0
#         p_dp = [[0] * n for _ in range(n)]

#         # Base case: Odd
#         for i in range(n):
#             p_dp[i][i] = True
#             max_length = 1
#             left = i
#             right = i+1

#         # Base case: Even
#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 p_dp[i][i+1] = True # base case
#                 max_length = 2
#                 left = i
#                 right = i+2

#         # Recursive case:
#         # P(i,j) = P(i+1,j−1) and S[i] == S[j]
#         # 採用『由上而下由左而右』進行搜索。
#         for j in range(n): # End
#             for i in range(j-1): # Start
#                 if s[i] == s[j] and p_dp[i+1][j-1]:
#                     p_dp[i][j] = True
#                     if j - i + 1 > max_length:
#                         left = i
#                         right = j+1
#                         max_length = j - i + 1

#         return s[left:right]


# Expand Around Center
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
        