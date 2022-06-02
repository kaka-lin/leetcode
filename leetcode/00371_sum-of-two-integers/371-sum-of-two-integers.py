class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == -b:
            return 0
    
        if abs(a) > abs(b):
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)
    
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
    
        return a