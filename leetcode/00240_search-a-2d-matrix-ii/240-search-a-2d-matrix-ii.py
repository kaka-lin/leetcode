# Solution: Linear Search from Top-Right Corner
# Time Complexity: O(m+n)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        
        # from bottom-left point 
        i = m - 1
        j = 0

        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
      
        return False
