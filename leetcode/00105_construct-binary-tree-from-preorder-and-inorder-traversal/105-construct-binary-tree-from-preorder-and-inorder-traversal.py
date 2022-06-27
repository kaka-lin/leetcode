# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder: (root,left,right):can find root 
        # inorder: (left,root,right): can find left and right
        if not preorder or not inorder:
            return None
        
        # root_val = preorder[0]
        # left_n =  inorder.index(root_val)
        root_val = preorder.pop(0)
        left_n = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, inorder[:left_n])
        root.right = self.buildTree(preorder, inorder[left_n+1:])
        
        return root
        