class MyQueue:
    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            front = self.queue[0]
            self.queue = self.queue[1:]
            return front
        
    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]
        else:
            return None
        
    def empty(self) -> bool:
        return True if not self.queue else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()