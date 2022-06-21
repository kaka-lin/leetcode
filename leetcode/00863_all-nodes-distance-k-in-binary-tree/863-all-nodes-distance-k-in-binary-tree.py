# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.dfs(root)
        ans = self.levelOrder(target, k)
        return ans
    
    # For Annotate Parent
    def dfs(self, node, parent=None):
        if node:
            node.parent = parent
            self.dfs(node.left, node)
            self.dfs(node.right, node)
    
    def levelOrder(self, target, k):
        queue = [[target, 0]]
        seen = {target} # set
        
        while queue:
            if queue[0][1] == k:
                return [node.val for node, depth in queue]
            node, depth = queue.pop(0)
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in seen:
                    queue.append((neighbor, depth+1))
                    seen.add(neighbor)
                
        return []
    