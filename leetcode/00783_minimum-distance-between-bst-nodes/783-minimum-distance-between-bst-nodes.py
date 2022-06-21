# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.orderd_array = []
        self.inorder(root)
        ans = self.compare(self.orderd_array)
        return ans
    
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        
        self.orderd_array.append(root.val)
        
        if root.right:
            self.inorder(root.right)
    
    def compare(self, array):
        min_num = array[1] - array[0]
        for i in range(1, len(array)-1):
            difference = array[i+1] - array[i]
            if min_num > difference:
                min_num = difference
        return min_num