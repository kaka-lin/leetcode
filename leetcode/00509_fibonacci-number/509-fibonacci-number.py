# Solution 1: Recursive (time limit exceeded)
# class Solution:
#     def fib(self, N: int) -> int:
#         if N < 2:
#             return N
#         else:
#             return self.fib(N-1) + self.fib(N-2)

# Solution 2: Recursive + Memoization
# class Solution:
#     def fib(self, N: int) -> int:
#         cache = {}
#        
#         def recur_fib(N):
#             if N in cache:
#                 return cache[N]
#            
#             if N < 2:
#                 result = N
#             else:
#                 result = recur_fib(N-1) + recur_fib(N-2)
#            
#             cache[N] = result
#             return result
#        
#         return recur_fib(N)

# Solution 3: DP
class Solution:
    def fib(self, N: int) -> int:
        cache = {0: 0, 1: 1}
        for n in range(2, N+1):
            cache[n] = cache[n-1] + cache[n-2]
        
        return cache[N]
