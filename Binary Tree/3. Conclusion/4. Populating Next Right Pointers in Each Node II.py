"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = deque([root])
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)     
                level.append(current)
            l = len(level)
            for i in range(l):
                if i+1 < l:
                    level[i].next = level[i+1]
                else:
                    level[i].next = None
        return root