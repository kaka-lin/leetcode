# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        stack = [root]
        level_stack = []
        level_ans = []
        
        while root and stack:
            while stack:
                root = stack.pop(0)
                level_ans.append(root.val)
                
                if root.left:
                    level_stack.append(root.left)
                
                if root.right:
                    level_stack.append(root.right)
            
            ans.append(level_ans)
            stack = level_stack
            level_stack = []
            level_ans = []

        return ans