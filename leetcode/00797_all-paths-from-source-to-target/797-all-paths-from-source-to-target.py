# Solution 1: BFS
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         n = len(graph)
#         start = 0
#         end = n - 1
        
#         path = [start]
#         queue = [[start, path]]
#         ans = []
        
#         while queue:
#             curr_node, path = queue.pop(0)
#             if curr_node == end:
#                 ans.append(path)
#                 continue
                
#             for neighbour in graph[curr_node]:
#                 level_path = path.copy()
#                 level_path.append(neighbour)
#                 queue.append([neighbour, level_path])
            
#         return ans
    

# Solution 2: DFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        start = 0
        end = n - 1
        
        result = []
        path = [start]
        self.DFS(start, end, graph, path, result)
        return result
    
    def DFS(self, node, end, graph, path, result):
        if node == end:
            result.append(path)
            return
        
        for neighbour in graph[node]:
            self.DFS(neighbour, end, graph, path+[neighbour], result)
            