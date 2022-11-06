class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges in 'graph'.
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = []
        visited = [False] * n
        
        queue = [source]
        visited[source] = True
        
        while queue:
            curr_node = queue.pop(0)
            if curr_node == destination:
                return True
            
            for neighbour in graph[curr_node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
                    
        return False
    