"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# Solution 1
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':  
#         if not root:
#             return root

#         node = root
#         queue = [node]
#         level_queue = []
#         while root and queue:
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

    
# Solution 2: BFS
# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return root
        
#         queue = [root]
#         while queue:
#             queue_length = len(queue)
#             for i in range(queue_length):
#                 node = queue.pop(0)
                
#                 # This check is important. We don't want to
#                 # establish any wrong connections. The queue will
#                 # contain nodes from 2 levels at most at any
#                 # point in time. This check ensures we only 
#                 # don't establish next pointers beyond the end
#                 # of a level
#                 if i < queue_length - 1:
#                     node.next = queue[0]
            
#                 if node.left: 
#                     queue.append(node.left)
            
#                 if node.right:
#                     queue.append(node.right)
                
#         return root


# Solution 3
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
