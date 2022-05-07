# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         length = len(s)
#         self.helper(s, 0, length)
#
#     def helper(self, s, i, length):
#         if i == (length // 2):
#             return
#         s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
#         self.helper(s, i+1, length)

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         length = len(s)
#         for i in range(length // 2): 
#             s[i], s[length - 1 -i] = s[length - 1 -i], s[i]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        prev, post = 0, len(s) - 1
        while prev < post:
            s[prev], s[post] = s[post], s[prev]
            prev, post = prev + 1, post - 1