class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        queue = [(sr, sc)]
        visited = {(sr, sc)}
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            r, c = queue.pop(0)
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                
                if image[x][y] == oldColor and (x, y) not in visited:
                    image[x][y] = newColor
                    queue.append((x, y))
                    visited.add((x, y))
        
        return image
