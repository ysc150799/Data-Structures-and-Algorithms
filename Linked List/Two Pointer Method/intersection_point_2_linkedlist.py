# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        lA = 0
        lB = 0
        while p1.next != None:
            lA+=1
            p1 = p1.next
        while p2.next != None:
            lB+=1
            p2 = p2.next
        p1 = headA
        p2 = headB
        if lA > lB:
            diff = lA - lB
            while diff != 0:
                p1 = p1.next
                diff -= 1
        else:
            diff = lB - lA
            while diff != 0:
                p2 = p2.next
                diff -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1