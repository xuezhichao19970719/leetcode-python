class Solution:
    def removeNthFromEnd(self, head, n):
        size = 0
        cur = p = head
        while cur.next:
            cur = cur.next
            size += 1
            if size > n:
                p = p.next
        if size + 1 == n:
            return  head.next
        else:
            p.next = p.next.next
            return head