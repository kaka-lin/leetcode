# [Not accepted]: Maximum recursion depth exceeded
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def helper(x, n, ans):
#             if n == 0:
#                 return ans
#            
#             return helper(x, n-1, ans * x)
#        
#         if n >= 0:
#             return helper(x, n, 1)
#         else:
#             return 1 / helper(x, -n, 1)
     

# Recursion    
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#        
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#        
#         if n % 2:
#             return x * self.myPow(x, n - 1)
#        
#         return self.myPow(x * x, n // 2)


# Iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1 / x
        
        ans = 1
        while n:
            if n & 1: # the same as n % 2
                ans *= x
            x *= x
            n >>= 1 # the same as n //= 2
            
        return ans