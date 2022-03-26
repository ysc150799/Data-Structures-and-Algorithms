# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == p or root == q:
            return root
        
        left_side = self.lowestCommonAncestor(root.left, p, q)
        right_side = self.lowestCommonAncestor(root.right, p, q)
        
        if not left_side and right_side:
            return right_side
        if left_side and not right_side:
            return left_side
        elif right_side and left_side:
            return root
        else:
            return None

'''
Iterative

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root:None}
        stack = [root]
        
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        return q

'''
        