# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorderlist = []
        self.inorder(root, inorderlist)
        sorted_in = sorted(set(inorderlist))
        if sorted_in == inorderlist:
            return True
        else:
            return False
        
    def inorder(self, node, inorderlist):
        if not node:
            return
        
        self.inorder(node.left, inorderlist)
        inorderlist.append(node.val)
        self.inorder(node.right, inorderlist)