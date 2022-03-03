# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preleft(self, root ,left):
        if root == None:
            left.append('null')
            return
        left.append(root.val)
        self.preleft(root.left,left)
        self.preleft(root.right,left)
    
    def preright(self, root ,right):
        if root == None:
            right.append('null')
            return
        right.append(root.val)
        self.preright(root.right, right)
        self.preright(root.left, right)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = [root.val]
        right = [root.val]
        self.preleft(root.left, left)
        self.preright(root.right, right)
        if left == right:
            return True
        else:
            return False
        