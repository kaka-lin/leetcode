# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.cache = {}
        return self.dfs(1, n)
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        if (start, end) in self.cache: 
            return self.cache[(start, end)]               
        
        tree_list = []
        for idx in range(start, end + 1):
            left_child = self.dfs(start, idx - 1)
            right_child = self.dfs(idx + 1, end)
            for left in left_child:
                for right in right_child:
                    root = TreeNode(idx)
                    root.left = left
                    root.right = right
                    tree_list.append(root)
        self.cache[(start, end)] = tree_list
        
        return tree_list
 