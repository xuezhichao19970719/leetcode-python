class Solution:
    def groupAnagrams(self, strs):
        h = {}
        for s in strs:
            h.setdefault(''.join(sorted(s)), []).append(s)
        return list(h.values())
                