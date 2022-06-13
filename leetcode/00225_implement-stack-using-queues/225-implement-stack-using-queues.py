class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        top = self.top()
        self.queue = self.queue[:-1]
        return top

    def top(self) -> int:
        if not self.empty():
            return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()