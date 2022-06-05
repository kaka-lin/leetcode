# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:       
#         # counts = {}
#         # for c in s:
#         #     if c not in counts:
#         #         counts[c] = 1
#         #     else:
#         #         counts[c] += 1
#         counts = collections.Counter(s)
        
#         for c in t:
#             if c not in counts:
#                 return c
#             else:
#                 if counts[c] == 0:
#                     return c
#                 else:
#                     counts[c] -= 1
        

# BITWISE method: XOR (^)
# hint: 自己 ^ 自己 = 0
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:  
        ans = 0
        for c in s:
            ans ^= ord(c)
        for c in t:
            ans ^= ord(c)   
        return chr(ans)