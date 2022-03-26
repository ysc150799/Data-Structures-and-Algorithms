# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #Recursive
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.buildSubTree(root, postorder, inorder)
        return root
    
    def buildSubTree(self, node, postorder, inorder):
        if not postorder or not inorder:
            return

        node.val = postorder.pop()
        in_index = inorder.index(node.val)
        
        if len(inorder[in_index+1:]) != 0:
            node.right = TreeNode()
            self.buildSubTree(node.right, postorder, inorder[in_index+1:])
        
        if len(inorder[0:in_index]) != 0:
            node.left = TreeNode() 
            self.buildSubTree(node.left, postorder, inorder[0:in_index])
        
    '''
    Iterative
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        memo = {}
        
        for idx,val in enumerate(inorder):
            memo[val] = idx
            
        
        i = len(postorder)-2
        
        
        root = TreeNode(postorder[-1])
        
        while(i >= 0):
            temp = root
            flag = True
            while(flag):
                
                a = memo[temp.val]
                
                b = memo[postorder[i]]
                
                if a < b:
                    
                    if temp.right is None:
                        temp.right = TreeNode(postorder[i])
                        flag = False
                    else:
                        temp = temp.right
                else:
                    if temp.left is None:
                        temp.left = TreeNode(postorder[i])
                        flag = False
                    else:
                        temp = temp.left
            i-=1
        
        
        return root
    '''
        
