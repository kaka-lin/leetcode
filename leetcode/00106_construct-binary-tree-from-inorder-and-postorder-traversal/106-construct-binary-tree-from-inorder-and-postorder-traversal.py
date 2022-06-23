# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: (left, root, right) => using the root we get to split left and right tree
        # postorder: (left, right, root) => get root 
        # 
        # in: 9 3 15 20 7 -> idx: 1, left: 9, right: 15,20,7
        # post: 9 15 7 20 3 -> root: 3
        if not inorder or not postorder:
            return None
        
        root_val = postorder[-1]
        # num_left = 0
        # for i in range(len(inorder)):
        #     if inorder[i] == root_node:
        #         num_left = i
        left_n = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:left_n], postorder[:left_n])
        root.right = self.buildTree(inorder[left_n+1:], postorder[left_n:-1])
        
        return root
        