class Solution:
    def removeNthFromEnd(self, head, n):
        size = 0
        cur = p = head
        while True:
            cur = cur.next
            size += 1
            if size > n:
                p = p.next
            if not cur.next:
                cur.next = head
                break
        if size == n:
            return  head
        else:
            return p
    def rotateRight(self, head, k):
        if not head:return []
        if not head.next: return head
        b = head
        c = 0
        while b.next:
            b = b.next
            c += 1
        k = k%(c+1)
        node = self.removeNthFromEnd(head, k)
        a = node.next
        node.next = None
        return a