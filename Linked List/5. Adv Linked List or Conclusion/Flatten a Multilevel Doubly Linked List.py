"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        parent_nodes = []
        itr = head
        
        while itr:
            if itr.child:
                parent_nodes.append(itr)
                itr = itr.child
            else:
                itr = itr.next
                
        for i in range(len(parent_nodes)):
            parent = parent_nodes.pop()
            itr = parent.child
            itr.prev = parent
            temp = parent.next
            parent.next = itr
            parent.child = None
            while itr.next:
                itr = itr.next
            itr.next = temp
            if temp:
                temp.prev = itr
        return head

'''
Good Iterative Solution


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        stack = [head]
        while stack:
            curr = stack.pop()
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev.next = curr
            curr.prev = prev
            prev= curr
        
        dummy.next.prev = None
        
        return dummy.next
'''