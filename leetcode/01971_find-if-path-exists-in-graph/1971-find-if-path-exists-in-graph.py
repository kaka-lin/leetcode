# Solution 1: BFS
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         graph = collections.defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        
#         queue = [source]
#         visited = set([source])
#         while queue:
#             curr_node = queue.pop(0)
#             if curr_node == destination:
#                 return True
            
#             # Add all neighbors to the queue.
#             for neighbor in graph[curr_node]:
#                 # Check if neighbor has been added to the queue before.
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)
        
#         # Our queue is empty and we did not reach the end node.
#         return False

    
# Solution DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:     
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        return self.DFS(source, destination, graph, visited)
    
    def DFS(self, curr_node, destination, graph, visited):
        if curr_node == destination:
            return True

        if curr_node not in visited:
            visited.add(curr_node)
            for neighbor in graph[curr_node]:     
                if self.DFS(neighbor, destination, graph, visited):
                    return True

        return False
        