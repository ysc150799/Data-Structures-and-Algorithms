# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False
        self.targetSum = 0
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.targetSum = targetSum
        curr_sum = 0
        self.pathSum(root,curr_sum)
        return self.flag
        
    def pathSum(self, node, curr_sum):
        if self.flag == True:
            return
        else:
            if not node:
                return None
            if not node.left and not node.right:
                if curr_sum + node.val == self.targetSum:
                    self.flag = True
            self.pathSum(node.left, curr_sum+node.val)
            self.pathSum(node.right, curr_sum+node.val)

'''
More Efficient Recursive Soution

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        if not root:
            return False
        
        targetSum -= root.val
        
        if not root.left and not root.right:
            if targetSum == 0:
                return True
        
        return (self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum))

'''