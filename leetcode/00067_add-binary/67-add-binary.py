# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         ans = ""
#         carry = 0
#         while a or b or carry:
#             if a and b:
#                 sum_ = int(a[-1]) + int(b[-1]) + carry
#             elif a:
#                 sum_ = int(a[-1]) + 0 + carry
#             elif b:
#                 sum_ = 0 + int(b[-1]) + carry
#             else:
#                 sum_ = carry
#                
#             if sum_ == 2:
#                 sum_ = 0
#                 carry = 1
#             elif sum_ == 3: # a:1, b:1, carry:1
#                 sum_ = 1
#                 carry = 1
#             else:
#                 carry = 0
#    
#             ans = str(sum_) + ans
#             a, b = a[:-1], b[:-1]
#             
#         return ans


# Pythonic
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:] # remove "0b"


# recursion
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0: return b
        if len(b) == 0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'