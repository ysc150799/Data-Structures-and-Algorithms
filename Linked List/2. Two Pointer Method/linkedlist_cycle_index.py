class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head             #fast pointer moving 2 increment ahead
        slow = head             #slow pointer moving 1 increment ahead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None