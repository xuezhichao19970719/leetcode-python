class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right, root.left= self.prev, None
        self.prev = root
        