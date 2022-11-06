class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS: rotten
        queue = []
        fresh_orange = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    fresh_orange += 1
        
        # Mark the round / level, _i.e_ the ticker of timestamp
        # use (-1, -1) represent finish when running BFS (queue)
        queue.append((-1, -1))

        minutes = -1
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            r, c = queue.pop(0)
            
            # We finish one round of processing
            if r == -1:
                minutes += 1
                if queue: # to avoid the endless loop
                    queue.append([-1, -1])
            else:
                for d in directions:
                    x = r + d[0]
                    y = c + d[1]
                
                    if x >= 0 and x < m and y >= 0 and y < n:
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            fresh_orange -= 1
                            queue.append([x, y])
        
        return minutes if fresh_orange == 0 else -1