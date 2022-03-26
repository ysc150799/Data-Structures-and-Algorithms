# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.buildSubTree(root, preorder, inorder)
        return root
    
    def buildSubTree(self, node, preorder, inorder):
        if not preorder or not inorder:
            return

        node.val = preorder.pop(0)
        in_index = inorder.index(node.val)
        
        if len(inorder[0:in_index]) != 0:
            node.left = TreeNode() 
            self.buildSubTree(node.left, preorder, inorder[0:in_index])
        
        if len(inorder[in_index+1:]) != 0:
            node.right = TreeNode()
            self.buildSubTree(node.right, preorder, inorder[in_index+1:])