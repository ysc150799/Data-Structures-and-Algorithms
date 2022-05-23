# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            curr = TreeNode(val = val)
            return curr
        node = root
        while True:
            if val < node.val:
                if not node.left:
                    curr = TreeNode(val = val)
                    node.left = curr
                    return root
                else:
                    node = node.left
            elif val > node.val:
                if not node.right:
                    curr = TreeNode(val = val)
                    node.right = curr
                    return root
                else:
                    node = node.right