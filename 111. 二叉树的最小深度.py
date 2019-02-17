class Solution(object):
    def minDepth(self, root):
        return 0 if not root else self.minDepth(root.left)+self.minDepth(root.right)+1 if not root.left or not root.right else min(self.minDepth(root.right),self.minDepth(root.left))+1