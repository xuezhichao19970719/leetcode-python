class Solution(object):
    def check(self, root):
        if root is None: return 0
        left, right  = self.check(root.left), self.check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    def isBalanced(self, root):
        return self.check(root) != -1