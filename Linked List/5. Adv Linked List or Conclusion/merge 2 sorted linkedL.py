# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge Cases
        if (list1 == None) and (list2 == None):
            return list1
        elif (list1 != None) and (list2 == None):
            return list1
        elif (list1 == None) and (list2 != None):
            return list2
        
        #Initialize
        if list1.val <= list2.val:
            list3 = list1
            head = list3
            list1 = list1.next
        else:
            list3 = list2
            head = list3
            list2 = list2.next
        
        #Main Code
        while (list1 != None) and (list2 != None):
            if list1.val <= list2.val:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        
        #Add Remaining Elements in LL
        if list1 != None:
            list3.next = list1
        
        if list2 != None:
            list3.next = list2
        
        return head

'''
Best Solution

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        dummy = ListNode(-1)
        curr = dummy
        i = list1
        j = list2
        while i and j:
            if i.val <= j.val:
                curr.next = i
                i = i.next
            else:
                curr.next = j
                j = j.next
            curr = curr.next
        while i:
            curr.next = i
            curr = curr.next
            i = i.next
        while j:
            curr.next = j
            curr = curr.next
            j = j.next
        return dummy.next
'''