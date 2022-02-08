class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        oddlink = head
        evenlink = head.next
        temp = evenlink
        while (oddlink != None and oddlink.next != None) and (evenlink != None and evenlink.next != None):
            oddlink.next = oddlink.next.next
            evenlink.next = evenlink.next.next
            oddlink = oddlink.next
            evenlink = evenlink.next
        oddlink.next = temp
        return head