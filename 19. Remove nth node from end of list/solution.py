class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current1 = head
        while current1:
            length += 1
            current1 = current1.next

        diff = abs(length-n)
        current1 = head
        count2 = 0
        if diff == 0:
            current1 = current1.next
            return current1

        while current1 and current1.next:
            if count2 == diff-1 and current1.next.next:
                current1.next = current1.next.next
                break
            elif count2 == diff-1 and current1.next.next == None:
                current1.next = None
            current1 = current1.next
            count2 += 1
        itr = head
        return itr
