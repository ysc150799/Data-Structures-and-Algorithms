# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        self.maxdepth(root,1)
        return self.max_depth
    
    def maxdepth(self,node,depth):
        if not node.left and not node.right:
            self.max_depth = max(self.max_depth,depth)
        else:
            if node.left: 
                self.maxdepth(node.left,depth+1)
            if node.right:
                self.maxdepth(node.right,depth+1)        
        
'''
Clean Recursive Solution

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if root is None:
            return 0
        res = max(self.maxDepth(root.right), self.maxDepth(root.left)) +1 
        return res
        
Iterative:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        level = []
        level.append(root)
        cnt = 0
        while level:
            cnt+=1
            nextlevel = []
            for i in level:
                if i.left != None:
                    nextlevel.append(i.left)
                if i.right != None:
                    nextlevel.append(i.right)
            level = nextlevel
        return cnt
'''    
