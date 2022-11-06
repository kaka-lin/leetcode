# BFS
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid)-1, len(grid[0])-1
        if grid[0][0] != 0 or grid[m][n] != 0:
            return -1
        
        # queue: [i, j, step]
        queue = [[0, 0, 1]]
        visited = set([0, 0])
        
        # BFS
        while queue:
            row, col, step = queue.pop(0)
            if (row, col) == (m, n):
                return step
            
            for x, y in self.get_neighbours(row, col, grid):
                if (x, y) not in visited: 
                    queue.append([x, y, step+1])
                    visited.add((x, y))
        
        return -1
                
    # Helper function to find the neighbors of a given cell.
    def get_neighbours(self, row, col, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), 
                      (0,1), (1,-1), (1,0), (1,1)]
        
        for d in directions:
            x = row + d[0]
            y = col + d[1]
            
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 0:
                yield (x, y)
