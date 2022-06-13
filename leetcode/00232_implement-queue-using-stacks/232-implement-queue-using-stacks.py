# class MyQueue:
#     def __init__(self):
#         self.queue = []
        
#     def push(self, x: int) -> None:
#         self.queue.append(x)

#     def pop(self) -> int:
#         if not self.empty():
#             front = self.queue[0]
#             self.queue = self.queue[1:]
#             return front
        
#     def peek(self) -> int:
#         if not self.empty():
#             return self.queue[0]
#         else:
#             return None
        
#     def empty(self) -> bool:
#         return True if not self.queue else False


# [Two Stacks]:
# Push - O(1) per operation
# Pop - Amortized O(1) per operation
#       Worst-case O(n)
class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:    
        self.peek()
        return self.output_stack.pop()
        
    def peek(self) -> int:     
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()