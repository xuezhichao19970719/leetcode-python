class Solution:
    def inorderTraversal(self, root):
        ans = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                root = tmpNode.right
        return ans