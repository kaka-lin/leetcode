# BFS: Time Limit Exceeded (2022/3/15 updqte)
#  Test Case:
#  [[1,1,1],[1,1,1],[1,1,1],[1,1,1],
#   [1,1,1],[1,1,1],[1,1,1],[1,1,1],
#   [1,1,1],[1,1,1],[1,1,1],[1,1,1],
#   [1,1,1],[1,1,1],[1,1,1],[1,1,1],
#   [1,1,1],[1,1,1],[1,1,1],[0,0,0]]
#
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 1:
#                     d = self.bfs(matrix, i, j)
#                     matrix[i][j] = d
      
#         return matrix
  
#     def bfs(self, matrix, r, c):
#         queue, visited = [], []
#         depth = 0
#         queue.append((r, c, depth))
#         visited.append((r, c, depth))
#         directions = [(0,1), (0,-1), (1,0), (-1,0)]
       
#         while queue:
#             r, c, dep = queue.pop(0)
#             for d in directions:
#                 x = r + d[0]
#                 y = c + d[1]
              
#                 if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
#                     continue
#                 else:
#                     if (x, y) not in visited:
#                         if matrix[x][y] == 0:
#                             return dep + 1                        
#                         queue.append((x, y, dep + 1))
#                         visited.append((x, y, dep + 1))


# Fast BFS Solution
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = []
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    queue.append([i, j])
                    visited.add((i, j))
        
        while queue:
            r, c = queue.pop(0)
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                if x >= 0 and x < m and y >= 0 and y < n:
                    if (x, y) not in visited:
                        matrix[x][y] = matrix[r][c] + 1                       
                        queue.append((x, y))
                        visited.add((x, y))
                        
        return matrix
                        