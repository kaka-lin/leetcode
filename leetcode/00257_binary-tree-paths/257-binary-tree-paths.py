# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:        
        ans = []
        path = []
        self.DFS(root, path, ans)
        return ans
    
    def DFS(self, root, path, ans):
        if not root:
            return 
        
        path.append(str(root.val))
        
        if not root.left and not root.right:
            ans.append("->".join(path))
        else:
            self.DFS(root.left, path, ans)
            self.DFS(root.right, path, ans)
        
        path.pop()
