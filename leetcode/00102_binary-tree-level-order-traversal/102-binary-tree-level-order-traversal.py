# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         ans = []
#         queue = [root]
#         level_queue = []
#         level_ans = []
        
#         while root and queue:
#             while queue:
#                 node = queue.pop(0)
#                 level_ans.append(node.val)
                
#                 if node.left:
#                     level_queue.append(node.left)
                
#                 if node.right:
#                     level_queue.append(node.right)
            
#             ans.append(level_ans)
#             queue = level_queue
#             level_queue = []
#             level_ans = []

#         return ans


# Solution 2: BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        queue = [root]
        while queue:
            # start the current level
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels.append(level)
        
        return levels
