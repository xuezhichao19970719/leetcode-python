class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        ans = i = 0
        for j,v in enumerate(s):
            if v in Dict:
                i = max(table[v], i)
            ans = max(ans, j - i + 1)
            Dict[v] = j + 1
        return ans