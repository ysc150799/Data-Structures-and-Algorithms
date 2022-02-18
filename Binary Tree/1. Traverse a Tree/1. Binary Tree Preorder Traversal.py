# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Iterative Solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:    
        
        if not root:
            return None
        
        result = []
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left: 
                stack.append(node.left)
                
        return result
        
'''
Recursive Solution

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        self.preOrder(root,result)
        return result
    
    def preOrder(self, node, result):
        if not node:
            return None
        result.append(node.val)
        self.preOrder(node.left,result)
        self.preOrder(node.right,result)
'''