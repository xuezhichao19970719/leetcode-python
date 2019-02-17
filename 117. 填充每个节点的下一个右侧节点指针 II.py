class Solution:
    def connect(self, root):
        prekid = kid = TreeLinkNode(0)
        while root:
            while root:
                kid.next = root.left
                kid = kid.next or kid
                kid.next = root.right
                kid = kid.next or kid
                root = root.next
            root, kid = prekid.next, prekid