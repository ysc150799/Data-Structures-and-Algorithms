# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_length(head:ListNode):
    curr = head
    length = 0
    if head == None:
        return 0
    while curr != None:
        curr = curr.next
        length += 1
    return length

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        index = get_length(head) - n
        if index == 0:
            head = head.next
        curr = head
        count = 0
        while curr != None:
            if count == index-1:
                curr.next = curr.next.next
                break
            curr = curr.next   
            count += 1
        return head
        