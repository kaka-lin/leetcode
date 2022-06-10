# Time Limit Exceeded
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         ans = [0] * len(temperatures)
#         for i in range(len(temperatures)):
#             curr = temperatures[i]
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[j] > curr:
#                     ans[i] = j - i
#                     break
#         return ans
  
    
# Monotonic Stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)
            
        return ans
                