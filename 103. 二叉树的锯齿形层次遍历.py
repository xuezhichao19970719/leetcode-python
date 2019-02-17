class Solution:
    def zigzagLevelOrder(self, root):
        i, ans, level = 0, [], [root]
        while level and root:
            ans.append([node.val for node in level][::(-1)**i])
            level = [leaf for n in level for leaf in (n.left, n.right) if leaf]
            i += 1
        return ans