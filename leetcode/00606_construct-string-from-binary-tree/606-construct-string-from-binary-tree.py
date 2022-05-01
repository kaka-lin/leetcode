# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        
        if t.left is None and t.right is None:
            return str(t.val) + ""
        
        if t.right is None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"