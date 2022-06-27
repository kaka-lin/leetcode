"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# BFS
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return None
        
#         node = root
#         queue = [node]
#         level_queue = []
#         while node and queue:
#             while queue:
#                 node = queue.pop(0)
#                 if queue:
#                     node.next = queue[0]
            
#                 if node.left: 
#                     level_queue.append(node.left)
            
#                 if node.right:
#                     level_queue.append(node.right)
            
#             queue = level_queue
#             level_queue = []
                
#         return root


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root
        
        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
            
        self.connect(root.left)
        self.connect(root.right)
        
        return root
