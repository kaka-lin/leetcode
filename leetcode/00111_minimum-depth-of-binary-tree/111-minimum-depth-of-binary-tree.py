# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = []
        visited = set()
        depth = 0
        queue.append((root, depth + 1))
        visited.add(root)
        
        while root:
            cur, depth = queue.pop(0)
            if not cur.left and not cur.right:
                return depth
            
            if cur.left and cur.left not in visited:
                queue.append((cur.left, depth + 1))
                visited.add(cur.left)

            if cur.right and cur.right not in visited:
                queue.append((cur.right, depth + 1))
                visited.add(cur.right)
        
        return depth
                