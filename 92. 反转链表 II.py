class Solution:
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        i = 1
        while i < m:
            p = p.next
            i += 1
        cur = p.next
        while i < n:
            x = p.next
            y = cur.next
            p.next = y
            cur.next = y.next
            y.next = x
            i += 1
        return dummy.next