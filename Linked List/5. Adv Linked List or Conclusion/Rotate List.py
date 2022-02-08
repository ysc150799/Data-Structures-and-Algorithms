# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def get_length(head):
    itr = head
    count = 0
    while itr != None:
        itr = itr.next
        count += 1
    return count
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 0:
            return head
        n = get_length(head)
        k = k % n
        if k == 0:
            return head
        curr = head
        for i in range(0,n-k-1):
            curr = curr.next
        init_pt = curr.next
        curr.next = None
        curr = init_pt
        while curr.next != None:
            curr = curr.next
        curr.next = head
        return init_pt