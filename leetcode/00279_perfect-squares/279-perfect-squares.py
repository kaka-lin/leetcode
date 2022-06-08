class Solution:
    def numSquares(self, n: int) -> int:
        # 0 -> 0
        # 1 -> 1
        # 2 -> 1 + 1
        # 3 -> 1 + 1 + 1
        if n <= 3: return n
        
        start = 0
        bfs_level = 0 # step
        queue = [(start, bfs_level)]
        visited = set([0])
        # square numbers <= n
        # 4*4 = 16 > target = 12
        # 所以會用到的 square 為: 1, 4, 9
        edges = [i*i for i in range(1, int(math.sqrt(n)) + 1)] 
        
        while queue:
            curr, bfs_level = queue.pop(0)
            for square in edges:
                new_val = curr + square
                if new_val == n:
                    return bfs_level + 1
                
                if new_val < n and new_val not in visited:
                    queue.append((new_val, bfs_level + 1))
                    visited.add(new_val)