"""
Init(): h,r = -1, [None, None, None]

                h,r
1. Enqueue(1): [1,  None, None]
                h  r
2. Enqueue(2): [1, 2, None]
                h     r    
3. Enqueue(3): [1, 2, 3]
                            
4. Enqueue(4): -> full
                     h  r
5. Dequeue(): [None, 2, 3]
                r  h
6. Enqueue(4): [4, 2, 3]

7. Enqueue(5): -> full

==> check full: (tail + 1) % size = head

               r        h
8. Dnqueue(): [4, None, 3]

               h,r        
9. Dnqueue(): [4,  None, None]

10. Dequeue(): h,r = -1, [None, None, None]

==> check empty: head = -1 or head == tail. let head = -1, tail = -1
"""


class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = 0
        
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.queue[self.head] = None
            self.head = -1
            self.tail = -1
            return True

        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1
        
    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == self.head
            
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()