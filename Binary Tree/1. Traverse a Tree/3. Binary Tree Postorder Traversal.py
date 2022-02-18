# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        stack = [(root, False)]
        result = []
        while stack:
            curr, vis = stack.pop()
            if curr:
                if vis:
                    result.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))            
        return result

'''
Recursive Solution

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        self.postorder(root,result)
        return result
    
    def postorder(self, node, result):
        if not node:
            return None
        self.postorder(node.left,result)
        self.postorder(node.right,result)
        result.append(node.val)
                
'''