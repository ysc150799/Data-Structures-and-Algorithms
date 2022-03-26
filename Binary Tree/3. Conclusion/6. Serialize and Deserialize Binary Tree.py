# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = [root]
        result = ""        
        while queue:
            node = queue.pop(0)
            if not node:
                result += "N,"
                continue
            result += str(node.val) + ","
            queue.append(node.left)
            queue.append(node.right)
        return result[:-1]
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if data[0] == '[]':
            return None
        root = TreeNode(int(data[0]))
        queue_pointer = 0
        value_pointer = 1
        queue = [root]
        while queue:
            node = queue.pop(0)
            value = data[value_pointer]
            value_pointer += 1
            
            if value != 'N':
                left = int(value)
                node.left = TreeNode(left)
                queue.append(node.left)
        
            value = data[value_pointer]
            value_pointer += 1
            
            if value != 'N':
                right = int(value)
                node.right = TreeNode(right)
                queue.append(node.right)  
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))