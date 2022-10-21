class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None
        while current:
            temp = current.next
            current.next = prev

            prev = current
            current = temp

        return prev
