# Using a Hash Set
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        doctor_advised = len(candyType) // 2
        types = set(candyType)
        return len(types) if doctor_advised > len(types) else doctor_advised
    