"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        curr = head
        while curr != None:
            node = Node(curr.val,curr.next,curr.random)
            curr.next = node
            curr = curr.next.next
        curr = head.next
        while curr.next != None:
            curr.random = curr.random.next if curr.random != None else None
            curr.next = curr.next.next
            curr = curr.next
        curr.random = curr.random.next if curr.random != None else None
        curr.next = None
        return head.next
