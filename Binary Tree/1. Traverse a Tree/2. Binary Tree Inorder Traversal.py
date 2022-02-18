# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        result = []
        stack = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                result.append(node.val)
                node = node.right
            else:
                break
        return result
            
'''
Recursive Solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        result = []
        self.inorder(root,result)
        return result
    
    def inorder(self, node, result):
        if not node:
            return None
        self.inorder(node.left,result)
        result.append(node.val)
        self.inorder(node.right,result)
'''

'''
2nd Iterative Solution

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        
        st = [(root, False)]
        out = []
        while st:
            curr, vis = st.pop()
            if curr:
                if vis:
                    out.append(curr.val)
                else:
                    st.append((curr.right, False))
                    st.append((curr, True))
                    st.append((curr.left, False))
        return out
'''