class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        nums_of_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    nums_of_island += 1
        
        return nums_of_island
    
    def bfs(self, matrix, r, c):
        queue = []
        visited = set()
        queue.append((r, c))
        visited.add((r, c))
        matrix[r][c] = "*"
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            r, c = queue.pop(0)
            
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                    continue
                else:
                    if (x, y) not in visited:
                        if matrix[x][y] == "1":
                            matrix[x][y] = "*"
                            queue.append((x, y))
                            visited.add((x, y))
