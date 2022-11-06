"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Solution 1
# class Solution:
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root:
#             return root
        
#         ans = []
#         queue = [root]
#         level_queue = []
#         level_ans = []
#         while root and queue:
#             while queue:
#                 node = queue.pop(0)
#                 level_ans.append(node.val)
                
#                 for children in node.children:
#                     level_queue.append(children)
            
#             ans.append(level_ans)
#             queue = level_queue
#             level_ans = []
#             level_queue = []
        
#         return ans


# Solutio 2: BFS
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        levels = []
        queue = [root]
        while queue:
            # start the current level
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            levels.append(level)
        
        return levels
    
    
    

    