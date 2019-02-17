class Solution:
    def isSymmetric(self, root):
        return self.compareNodeVal(root, root)
    def compareNodeVal(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        else:
            return self.compareNodeVal(root1.left, root2.right) and self.compareNodeVal(root1.right, root2.left) if root1.val == root2.val else False