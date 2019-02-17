class Solution:
    def partition(self, head, x):
        m = a = ListNode(0)
        n = b = ListNode(0)
        while head:
            if head.val < x:
                a.next = head
                a = a.next
            else:
                b.next = head
                b = b.next
            head = head.next
        b.next = None
        a.next = n.next
        return m.next