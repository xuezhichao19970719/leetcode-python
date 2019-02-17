class Solution:
    def combinationSum(self, candidates, target):
        m = [[] for i in range(target)]
        for n in candidates:
            if target - n > -1:
                m[target - n].append([n])
            for s in range(target-1, n-1, -1):
                for entry in m[s]:
                    m[s - n].append(entry + [n])
        return m[0]
