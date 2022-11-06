class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        start = 0
        end = n - 1
        
        path = [start]
        queue = [[start, path]]
        ans = []
        
        while queue:
            curr_node, path = queue.pop(0)
            if curr_node == end:
                ans.append(path)
                continue
                
            for neighbour in graph[curr_node]:
                level_path = path.copy()
                level_path.append(neighbour)
                queue.append([neighbour, level_path])
            
        return ans