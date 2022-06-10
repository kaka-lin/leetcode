# [缺點]: 很慢
# class MinStack:
#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         if not self.stack:
#             return
#         self.stack.pop()

#     def top(self) -> int:
#         if not self.stack:
#             return False
#         return self.stack[-1]

#     def getMin(self) -> int:
#         min_num = math.inf
#         for num in self.stack:
#             if num < min_num:
#                 min_num = num
#         return min_num


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        # 每一次 push 都放兩個值
        # (prev, top): (目前的最小值, 當次 push 的值)
        if self.stack:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)
        
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return self.stack[-2]
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()