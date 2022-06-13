# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:  
        if not subRoot:
            return True
        
        return self.dfs(root, subRoot)
        
    def dfs(self, root, subRoot):
        if not root:
            return False
            
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
            
        return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)
    
    
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and \
                   self.isSameTree(p.right, q.right)
    