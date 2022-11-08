# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key == root.val:
            if root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                # deletion of nodes with 2 children
                # find the inorder successor and replace the current node
                # inorder successor: 為右子樹中的最小值
                min_node = self.findMinimum(root.right)
                root.val = min_node.val
                # ** key step ** recurse on root.right but with `key = root.val` (min val in right subtree)
                root.right = self.deleteNode(root.right, root.val)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
    
    def findMinimum(self, root):
        while (root.left):
            root = root.left
        return root