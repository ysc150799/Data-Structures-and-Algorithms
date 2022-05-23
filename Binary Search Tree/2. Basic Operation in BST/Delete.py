# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_successor(self,node):
        if node.right:
            parent = node
            node = node.right
        else:
            return None,None
        
        while node.left:
            parent = node
            node = node.left
        return parent,node
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        node = root
        parent = TreeNode(-1,root,None)
        head = parent
        
        #Search node with key
        while node:
            if node.val > key:
                parent = node
                node = node.left
            elif node.val < key:
                parent = node
                node = node.right
            else:
                break
        #If key does not exist
        if not node:
            return root 
        
        #Find Inorder Successor
        par,successor = self.inorder_successor(node)
        
        #If no inorder successor is present in child node's
        if not par and not successor:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return head.left
        
        #Delete key and replace with inorder successor
        if par == node:
            if parent.left == node:
                parent.left = successor
            else:
                parent.right = successor
            successor.left = node.left
        else:
            par.left = successor.right
            if parent.left == node:
                parent.left = successor
            else:
                parent.right = successor
            successor.left = node.left
            successor.right = node.right
        return head.left
        
                            
                    