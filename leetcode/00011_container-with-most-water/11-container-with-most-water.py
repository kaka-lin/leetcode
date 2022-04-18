class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        front = 0
        end = len(height) - 1
        
        while front < end:
            w = end - front
             
            if height[front] < height[end]:
                h = height[front]
                front += 1
            else:
                h = height[end]
                end -= 1
            
            area = w * h
            if area > max_area:
                max_area = area
        
        return max_area