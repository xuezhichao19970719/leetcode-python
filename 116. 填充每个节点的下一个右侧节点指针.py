class Solution:
    def connect(self, root):
        if not root: return 
        while root.left:
            level=root.left
            while root:
                root.left.next=root.right
                cur=root.right
                root=root.next
                if cur and root:
                    cur.next=root.left
            root=level