"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# DFS iteratively
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':    
        if not node:
            return
        
        clone_node = Node(node.val)
        stack = [node]
        visited = {node: clone_node} 
        
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    clone_neighbor = Node(neighbor.val)
                    visited[node].neighbors.append(clone_neighbor)
                    visited[neighbor] = clone_neighbor
                    stack.append(neighbor)
                else:
                    visited[node].neighbors.append(visited[neighbor])
                
        return clone_node
