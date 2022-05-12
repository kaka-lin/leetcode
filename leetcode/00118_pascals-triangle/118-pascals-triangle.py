# Dynamic Programming
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_list = []
        for row in range(numRows):
            pascal_list.append([0] * (row+1))
            for col in range(len(pascal_list[row])):
                self.helper(row, col, pascal_list)
        
        return pascal_list
            
    def helper(self, nr, nc, pascal_list):
        if nc == 0 or nc == nr:
            pascal_list[nr][nc] = 1
        else:
            pascal_list[nr][nc] = pascal_list[nr - 1][nc - 1] \
                                + pascal_list[nr - 1][nc]
            